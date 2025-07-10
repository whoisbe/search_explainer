import ollama
import duckdb
import argparse

MODEL_NAME = 'mxbai-embed-large'

# takes a query and returns the most relevant movie titles and overviews
def vector_search(query: str, con: duckdb.DuckDBPyConnection):
    """
    Perform a vector search on the movie embeddings to find the most relevant titles and overviews.
    """
    # Generate the query embedding
    query_embedding = ollama.embed(model=MODEL_NAME, input=[query])['embeddings'][0]
    # print(type(query_embedding), len(query_embedding))

    # Search for the most similar movie embeddings
    results = con.sql(
        """SELECT title, overview, 
        array_cosine_similarity(overview_embeddings::FLOAT[1024], $query_embedding::FLOAT[1024]) AS score
        FROM movies ORDER BY score DESC LIMIT 5""",
        params={"query_embedding": query_embedding}
    ).fetchall()

    return results

if __name__ == "__main__":
    # Connect to the DuckDB database
    con = duckdb.connect(database='movies.duckdb', read_only=True)
    parser = argparse.ArgumentParser(description="Vector Search for Movies")
    parser.add_argument('query', type=str, help='Search query for movie overviews')
    args = parser.parse_args()

    # Perform the vector search
    results = vector_search(args.query, con)
    for result in results:
        print(f"Title: {result[0]}\nOverview: {result[1]}\nScore: {result[2]:.4f}\n")
    # Close the database connection
    print("✅ Vector search completed.")
    con.close()
    
    