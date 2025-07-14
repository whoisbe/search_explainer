import duckdb
import ollama
from tqdm import tqdm
from utils.schema import get_connection, add_embedding_columns

DEFAULT_MODEL_NAME = 'mxbai-embed-large'
DEFAULT_BATCH_SIZE = 100

def check_and_pull_model(model_name=DEFAULT_MODEL_NAME):
    print(f"🔎 Checking for Ollama model '{model_name}'...")
    try:
        local_models = [m['model'] for m in ollama.list()['models']]
        if f"{model_name}:latest" not in local_models:
            print(f"⬇️ Pulling '{model_name}'...")
            for chunk in ollama.pull(model_name, stream=True):
                if 'status' in chunk:
                    print(f"Status: {chunk['status']}", end='\r')
            print(f"\n✅ Model '{model_name}' ready.")
        else:
            print(f"ℹ️ Model '{model_name}' already available locally.")
    except Exception as e:
        print(f"❌ Error with Ollama: {e}")
        print("Ensure Ollama is running locally.")
        exit(1)

def generate_and_store_embeddings(con, model_name=DEFAULT_MODEL_NAME, batch_size=DEFAULT_BATCH_SIZE):
    total_rows = con.sql("SELECT COUNT(*) FROM movies").fetchone()[0]
    pending_rows = con.sql(
        "SELECT COUNT(*) FROM movies WHERE title_embeddings IS NULL OR overview_embeddings IS NULL"
    ).fetchone()[0]

    print(f"📊 Total movies: {total_rows}")
    print(f"🔍 Movies needing embeddings: {pending_rows}")

    if pending_rows == 0:
        print("✅ All movies already have embeddings. No updates needed.")
        return

    print(f"📝 Generating embeddings for {pending_rows} movies...")

    with tqdm(total=pending_rows, desc="Embedding Movies", unit="movie") as pbar:
        while True:
            batch = con.sql(
                f"""
                SELECT id, title, overview 
                FROM movies 
                WHERE title_embeddings IS NULL OR overview_embeddings IS NULL 
                LIMIT {batch_size}
                """
            ).fetchdf()

            if batch.empty:
                break

            ids = batch['id'].tolist()
            titles = batch['title'].fillna('').tolist()
            overviews = batch['overview'].fillna('').tolist()

            try:
                title_emb = ollama.embed(model=model_name, input=titles)['embeddings']
                overview_emb = ollama.embed(model=model_name, input=overviews)['embeddings']
            except Exception as e:
                print(f"❌ Error during embedding: {e}")
                break

            for i in range(len(ids)):
                con.execute(
                    "UPDATE movies SET title_embeddings = ?, overview_embeddings = ? WHERE id = ?",
                    [title_emb[i], overview_emb[i], ids[i]]
                )

            pbar.update(len(ids))

    print("✅ Embedding generation complete and database updated.")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Embedding Generator for Movies Dataset")
    parser.add_argument('--model', type=str, default=DEFAULT_MODEL_NAME, help='Ollama model name')
    parser.add_argument('--batch_size', type=int, default=DEFAULT_BATCH_SIZE, help='Batch size for embedding generation')

    args = parser.parse_args()

    check_and_pull_model(args.model)
    con = get_connection()
    add_embedding_columns(con)
    generate_and_store_embeddings(con, model_name=args.model, batch_size=args.batch_size)

    print("\n🔎 Sample rows with embeddings:")
    con.sql("""
        SELECT id, title, list_slice(title_embeddings, 1, 5) AS title_emb_sample 
        FROM movies 
        WHERE title_embeddings IS NOT NULL 
        LIMIT 5
    """).show()

    con.close()