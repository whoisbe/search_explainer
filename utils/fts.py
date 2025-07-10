# utils/fts.py

import duckdb
from utils.schema import get_connection

DEFAULT_TABLE = 'movies'
DEFAULT_INDEX_NAME = 'fts_main_movies'
DEFAULT_FIELDS = ['id', 'title', 'overview']

def install_and_load_fts(con):
    """
    Ensure FTS extension is installed and loaded.
    """
    print("⚙️ Installing/loading FTS extension...")
    con.sql("INSTALL 'fts';")
    con.sql("LOAD 'fts';")
    print("✅ FTS extension ready.")

def create_fts_index(con, table=DEFAULT_TABLE, fields=DEFAULT_FIELDS):
    """
    Create a full-text search index on the specified table and fields.
    """
    install_and_load_fts(con)
    field_str = "', '".join(fields[1:])  # skip id column from fields list
    id_col = fields[0]
    sql = f"PRAGMA create_fts_index('{table}', '{id_col}', '{field_str}');"
    con.sql(sql)
    print(f"✅ FTS index created on '{table}' for fields: {', '.join(fields[1:])}.")

if __name__ == "__main__":
    con = get_connection()
    create_fts_index(con)
    con.close()
