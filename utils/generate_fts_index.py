# connect to movies.duckdb database
# install and load fts extension
# PRAGMA create_fts_index('movies', 'id', 'title', 'overview');

import duckdb

con = duckdb.connect(database='movies.duckdb', read_only=False)
con.sql("INSTALL 'fts';")
con.sql("LOAD 'fts';")

def create_fts_index(con: duckdb.DuckDBPyConnection):
    """
    Create a full-text search index on the 'movies' table.
    """
    con.sql("PRAGMA create_fts_index('movies', 'id', 'title', 'overview');")
    print("✅ Full-text search index created successfully.")

if __name__ == "__main__":
    create_fts_index(con)
    con.close()