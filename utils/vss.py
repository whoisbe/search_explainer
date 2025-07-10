# utils/vss.py

import duckdb
import ollama
import argparse
from utils.schema import get_connection

DEFAULT_MODEL_NAME = 'mxbai-embed-large'
DEFAULT_TABLE = 'movies'

def vector_search(query, con, model_name=DEFAULT_MODEL_NAME, table=DEFAULT_TABLE, limit=5):
    """
    Perform a vector similarity search on embeddings in DuckDB.
    """
    try:
        query_embedding = ollama.embed(model=model_name, input=[query])['embeddings'][0]
    except Exception as e:
        print(f"❌ Error generating query embedding: {e}")
        print("Ensure Ollama is running and model is available.")
        return []

    sql = f"""
        SELECT title, overview,
        array_cosine_similarity(overview_embeddings::FLOAT[1024], $query_embedding::FLOAT[1024]) AS score
        FROM {table}
        ORDER BY score DESC
        LIMIT {limit}
    """
    results = con.sql(sql, params={"query_embedding": query_embedding}).fetchall()
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Vector Similarity Search Utility")
    parser.add_argument('query', type=str, help='Search query text')
    parser.add_argument('--model', type=str, default=DEFAULT_MODEL_NAME, help='Ollama model name')
    parser.add_argument('--limit', type=int, default=5, help='Limit number of results (default: 5)')

    args = parser.parse_args()

    con = get_connection(readonly=True)
    results = vector_search(args.query, con, model_name=args.model, limit=args.limit)

    for title, overview, score in results:
        print(f"🎬 Title: {title}\n📝 Overview: {overview}\n⭐ Score: {score:.4f}\n{'-'*40}")

    con.close()
