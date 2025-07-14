# 📚 Full-Text Search (FTS) with DuckDB

## 🚀 Example Scenario

Let’s say we want to find movies about **space exploration**.  
Lexical search can’t help us much—it’s too literal. For example:

- `"space exploration"` will match only exact phrases
- `"journey to the stars"` or `"exploring the cosmos"` would be ignored

🔔 **Full-Text Search (FTS)** enables smarter, relevance-ranked search using tokenization, stemming, and BM25 scoring.

---

## 🛠️ Prerequisites

Ensure the database and FTS index are ready:

```bash
python utils/schema.py       # Load dataset
python utils/fts.py          # Install extension + create FTS index
```

---

## 🔍 Example FTS Query in SQL

```sql
SELECT 
    fts_main_movies.match_bm25(id, 'space exploration', fields := 'overview') AS score,
    title, overview
FROM movies
WHERE score IS NOT NULL
ORDER BY score DESC
LIMIT 10;
```

This query:
- ✅ Searches the `overview` column
- ✅ Ranks results by relevance
- ✅ Orders results descending by score

---

## 🐍 Python Example

We’ve included a utility script for this in `utils/fts_search.py`.

⚠️ **Run it as a module to avoid import issues:**

```bash
python -m utils.fts_search "space exploration" --limit 5 --fields overview
```

---

## 🎯 Key Takeaways

- FTS enables much smarter search than lexical string matching
- Supports relevance ranking with BM25 algorithm
- Great for ranking documents by keyword density and distribution

👉 [Next: Vector Similarity Search ➡️](04_vector_search.md)