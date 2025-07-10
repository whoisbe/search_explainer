# load_data.py

import duckdb

def load_database():
    """
    Load the DuckDB database and return the connection.
    """
    # Connect to the DuckDB database
    con = duckdb.connect(database='movies.duckdb', read_only=False)
    con.sql("""
            CREATE TABLE IF NOT EXISTS movies AS FROM read_csv_auto('../data/moviesData.csv')
            """)
    print("✅ Database loaded successfully.")
    return con

def add_embedding_columns(con):
    """
    Alters the 'movies' table to add columns for title and overview embeddings if they don't exist.
    """
    all_columns = {c[0] for c in con.sql("DESCRIBE 'movies'").fetchall()}

    columns_to_add = {
        'title_embeddings': 'FLOAT[]',
        'overview_embeddings': 'FLOAT[]'
    }

    for col_name, col_type in columns_to_add.items():
        if col_name not in all_columns:
            con.sql(f"ALTER TABLE movies ADD COLUMN {col_name} {col_type};")
            print(f"✅ Added '{col_name}' column.")
        else:
            print(f"ℹ️ '{col_name}' column already exists.")

if __name__ == "__main__":
    # Load the database and print a sample of the data
    db_connection = load_database()
    add_embedding_columns(db_connection)

    print("\nSample data from 'movies' table after schema update:")
    db_connection.sql("SELECT * FROM movies USING SAMPLE 5 ROWS").show()
    db_connection.close()