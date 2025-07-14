# utils/lexical_search.py

import duckdb
import argparse
from utils.schema import get_connection

DEFAULT_TABLE = 'movies'

def lexical_search(query, con, table=DEFAULT_TABLE, limit=10):
    sql = f"""
        SELECT id, title, overview
        FROM {table}
        WHERE LOWER(title) LIKE '%' || LOWER($query) || '%'
        LIMIT {limit}
    """
    return con.sql(sql, params={"query": query}).fetchall()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lexical Search Utility")
    parser.add_argument("query", type=str, help="Search query text")
    parser.add_argument("--limit", type=int, default=10, help="Limit results (default 10)")
    args = parser.parse_args()

    con = get_connection(readonly=True)
    results = lexical_search(args.query, con, limit=args.limit)

    for row in results:
        print(f"🎬 {row[1]} (ID: {row[0]})\n📝 {row[2]}\n{'-'*40}")

    con.close()