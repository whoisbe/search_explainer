# Connect to movies.duckdb database
# Takes an argument for query 
# perform full text search using the fts_main_movies.match_bm25 function
# Example SQL query:
# SELECT fts_main_movies.match_bm25(id, 'adventure', fields := 'overview') AS score, title, overview FROM movies WHERE score IS NOT NULL ORDER BY score DESC;

import duckdb
import argparse

con = duckdb.connect(database='movies.duckdb', read_only=True)
def full_text_search(query: str, con: duckdb.DuckDBPyConnection):
    """
    Perform a full text search on the movie titles and overviews.
    """
    results = con.sql(
        """SELECT fts_main_movies.match_bm25(id, $query, fields := 'overview') AS score, title, overview 
           FROM movies 
           WHERE score IS NOT NULL 
           ORDER BY score DESC""",
        params={"query": query}
    ).fetchall()
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Full Text Search for Movies")
    parser.add_argument('query', type=str, help='Search query for movie titles and overviews')
    args = parser.parse_args()
    # Perform the full text search
    results = full_text_search(args.query, con)
    for result in results:
        print(f"Score: {result[0]:.4f}, Title: {result[1]}\nOverview: {result[2]}\n")
    # Close the database connection
    