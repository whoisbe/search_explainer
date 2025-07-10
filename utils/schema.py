# utils/schema.py

import duckdb
import os
import pandas as pd

DEFAULT_DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "movies.duckdb"))
DEFAULT_DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "moviesData.csv"))

def get_connection(db_path=DEFAULT_DB_PATH, readonly=False):
    """
    Get a DuckDB connection.
    """
    con = duckdb.connect(database=db_path, read_only=readonly)
    return con

def load_movies_table(con, csv_path=DEFAULT_DATA_PATH):
    """
    Load moviesData.csv into DuckDB as 'movies' table.
    """
    print(f"📥 Loading dataset from {csv_path}")
    if not os.path.exists(csv_path):
        print(f"❌ Dataset file not found at {csv_path}")
        return

    con.sql(f"""
        CREATE TABLE IF NOT EXISTS movies AS FROM read_csv_auto('{csv_path}')
    """)
    print("✅ 'movies' table loaded.")

def add_embedding_columns(con):
    """
    Add embedding columns to 'movies' table if they don't exist.
    """
    columns = {c[0] for c in con.sql("DESCRIBE 'movies'").fetchall()}

    for col in ['title_embeddings', 'overview_embeddings']:
        if col not in columns:
            con.sql(f"ALTER TABLE movies ADD COLUMN {col} FLOAT[]")
            print(f"✅ Added column '{col}'")
        else:
            print(f"ℹ️ Column '{col}' already exists")

if __name__ == "__main__":
    con = get_connection()
    load_movies_table(con)
    add_embedding_columns(con)

    print("\n🔎 Sample rows from 'movies' table:")
    con.sql("SELECT id, title FROM movies USING SAMPLE 5 ROWS").show()
    con.close()
