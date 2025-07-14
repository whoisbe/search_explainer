# 🔤 Lexical Search — Tutorial

## 🎯 Objective
Introduce **lexical search** fundamentals using plain string matching and demonstrate how to query the `movies` dataset for exact or partial matches before introducing more advanced search paradigms.

---

## 🔍 What is Lexical Search?
Lexical search is the simplest form of search: it directly compares query terms with stored text. It's often case-insensitive and may use substring matching but lacks ranking or semantic understanding.

---

## ⚙️ Setup
Make sure your environment is ready:
```bash
python utils/dataset.py          # Download dataset
python utils/schema.py           # Load dataset into DuckDB
```

---

## 📝 Example Query
In **DuckDB SQL**, lexical search can look like this:
```sql
SELECT id, title, overview
FROM movies
WHERE LOWER(title) LIKE '%alien%'
LIMIT 10;
```

This matches any movie where `title` contains "alien" (case-insensitive).

---

## 🐍 Python Example
We’ve provided a convenient script for this in `utils/lexical_search.py`:

```bash
python utils/lexical_search.py "alien" --limit 10
```

Example code:
```python
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
```

---

## 🚀 Key Takeaways
- Lexical search is easy to implement but limited: it doesn't handle ranking, typos, or semantics.
- Ideal as a baseline before introducing FTS and vector search.

👉 [Next: Full-Text Search ➡️](03_full_text_search.md)
