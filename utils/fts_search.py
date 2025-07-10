# utils/fts_search.py

import duckdb
import argparse
from utils.schema import get_connection

DEFAULT_TABLE = 'movies'

def full_text_search(query, con, table=DEFAULT_TABLE, fields='overview', limit=10):
    """
    Perform full-text search using match_bm25 on specified fields.
    """
    sql = f"""
        SELECT 
            fts_main_{table}.match_bm25(id, $query, fields := '{fields}') AS score, 
            title, overview
        FROM {table}
        WHERE score IS NOT NULL
        ORDER BY score DESC
        LIMIT {limit}
    """
    results = con.sql(sql, params={"query": query}).fetchall()
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Full-Text Search Utility")
    parser.add_argument('query', type=str, help='Search query text')
    parser.add_argument('--limit', type=int, default=10, help='Limit number of results (default: 10)')
    parser.add_argument('--fields', type=str, default='overview', help='Fields to search (default: overview)')

    args = parser.parse_args()

    con = get_connection(readonly=True)
    results = full_text_search(args.query, con, fields=args.fields, limit=args.limit)

    for score, title, overview in results:
        print(f"🔹 Score: {score:.4f}\n🎬 Title: {title}\n📝 Overview: {overview}\n{'-'*40}")

    con.close()
