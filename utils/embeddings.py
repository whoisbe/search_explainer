# utils/embeddings.py

import duckdb
import ollama
from tqdm import tqdm
from utils.schema import get_connection, add_embedding_columns

DEFAULT_MODEL_NAME = 'mxbai-embed-large'
DEFAULT_BATCH_SIZE = 100

def check_and_pull_model(model_name=DEFAULT_MODEL_NAME):
    """
    Check if Ollama model exists locally and pull if not.
    """
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
    """
    Generate embeddings for titles and overviews and store in DuckDB.
    """
    count = con.sql(
        "SELECT COUNT(*) FROM movies WHERE title_embeddings IS NULL OR overview_embeddings IS NULL"
    ).fetchone()[0]

    if count == 0:
        print("✅ All records already have embeddings.")
        return

    print(f"📝 Generating embeddings for {count} movies...")

    with tqdm(total=count, desc="Embedding Movies", unit="movie") as pbar:
        while True:
            batch = con.sql(
                f"SELECT id, title, overview FROM movies WHERE title_embeddings IS NULL OR overview_embeddings IS NULL LIMIT {batch_size}"
            ).fetchdf()

            if batch.empty:
                break

            ids = batch['id'].tolist()
