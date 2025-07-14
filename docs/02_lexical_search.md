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
```python
import duckdb
from utils.schema import get_connection

def lexical_search(query, con, limit=10):
    sql = f"""
        SELECT id, title, overview
        FROM movies
        WHERE LOWER(title) LIKE '%' || LOWER($query) || '%'
        LIMIT {limit}
    """
    results = con.sql(sql, params={"query": query}).fetchall()
    return results

if __name__ == "__main__":
    con = get_connection(readonly=True)
    query = "alien"
    results = lexical_search(query, con)

    for row in results:
        print(f"🎬 {row[1]} (ID: {row[0]})\n📝 {row[2]}\n{'-'*40}")

    con.close()
```

---

## 🚀 Key Takeaways
- Lexical search is easy to implement but limited: it doesn't handle relevance ranking, typos, or semantics.
- Ideal as a baseline or fallback mechanism before introducing FTS and vector search.

✅ Next step: Upgrade to **full-text search using DuckDB’s FTS extension**.

👉 [Proceed to Full Text Search Tutorial ➡️](#)