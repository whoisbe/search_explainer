import ollama
import duckdb
from tqdm import tqdm
from load_data import load_database, add_embedding_columns

MODEL_NAME = 'mxbai-embed-large'
BATCH_SIZE = 100  # Process 100 movies at a time

def check_and_pull_model(model_name: str):
    """
    Checks if the Ollama model is available locally and pulls it if not.
    """
    print(f"Checking for model '{model_name}'...")
    try:
        # ollama.list() returns models with tags, e.g., 'nomic-embed-text:latest'
        local_models = [m['model'] for m in ollama.list()['models']]
        if f"{model_name}:latest" not in local_models:
            print(f"Model '{model_name}' not found locally. Pulling from Ollama...")
            # stream=True gives us progress updates
            stream = ollama.pull(model_name, stream=True)
            for chunk in stream:
                if 'total' in chunk and 'completed' in chunk:
                    percent = (chunk['completed'] / chunk['total']) * 100
                    print(f"Status: {chunk['status']} - {percent:.2f}% complete", end='\r')
                else:
                    # Print status without progress if not available
                    print(f"Status: {chunk['status']}", end='\r')
            print("\n✅ Model pulled successfully.")
        else:
            print(f"ℹ️ Model '{model_name}' is already available.")
    except Exception as e:
        print(f"\n❌ Error interacting with Ollama: {e}")
        print("Please ensure the Ollama application is running.")
        exit(1)

def generate_and_store_embeddings(con: duckdb.DuckDBPyConnection, model_name: str, batch_size: int):
    """
    Generates embeddings for movie titles and overviews and stores them in the database.
    """
    # Get the count of movies that need embeddings
    query = "SELECT count(*) FROM movies WHERE title_embeddings IS NULL OR overview_embeddings IS NULL"
    total_movies_to_process = con.execute(query).fetchone()[0]

    if total_movies_to_process == 0:
        print("✅ All movies already have embeddings. Nothing to do.")
        return

    print(f"Found {total_movies_to_process} movies to process. Generating embeddings...")

    with tqdm(total=total_movies_to_process, desc="Embedding Movies", unit="movie") as pbar:
        while True:
            # Fetch a batch of movies without embeddings
            batch_df = con.execute(
                f"SELECT id, title, overview FROM movies WHERE title_embeddings IS NULL OR overview_embeddings IS NULL LIMIT {batch_size}"
            ).fetchdf()

            if batch_df.empty:
                break  # No more movies to process

            ids = batch_df['id'].tolist()
            titles = batch_df['title'].fillna('').tolist()
            overviews = batch_df['overview'].fillna('').tolist()

            # Generate embeddings for titles and overviews in batch
            title_embeddings = ollama.embed(model=model_name, input=titles)['embeddings']
            overview_embeddings = ollama.embed(model=model_name, input=overviews)['embeddings']

            # Update the database with the new embeddings using prepared statements
            for i in range(len(ids)):
                con.execute(
                    "UPDATE movies SET title_embeddings = ?, overview_embeddings = ? WHERE id = ?",
                    [title_embeddings[i], overview_embeddings[i], ids[i]]
                )

            pbar.update(len(ids))

    print("\n✅ Successfully generated and stored all embeddings.")

if __name__ == "__main__":
    check_and_pull_model(MODEL_NAME)
    db_connection = load_database()
    add_embedding_columns(db_connection)
    generate_and_store_embeddings(db_connection, MODEL_NAME, BATCH_SIZE)
    print("\nSample data from 'movies' table with new embeddings:")
    db_connection.sql("SELECT id, title, list_slice(title_embeddings, 1, 5) as title_emb_sample FROM movies WHERE title_embeddings IS NOT NULL LIMIT 5").show()
    db_connection.close()