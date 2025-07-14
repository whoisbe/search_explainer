# 🧠 Vector Similarity Search with DuckDB + Ollama

## 🚀 Example Scenario

What if we want to search for **movies “about astronauts and distant galaxies”**, but not necessarily containing those exact words?  
Traditional keyword or FTS approaches struggle with semantic similarity.

🔔 **Vector Similarity Search (VSS)** solves this by encoding text into high-dimensional embeddings and finding records that are *close* in vector space — enabling search by meaning, not exact words.

---

## 🛠️ Prerequisites

Ensure your dataset is loaded and embeddings are generated:

```bash
python -m utils.schema         # Load dataset
python -m utils.embeddings     # Generate embeddings (requires Ollama running)
```

☕ **Note:** Generating embeddings for ~8,500 movie records can take a while (e.g., ~18 minutes on an M1 Mac). Perfect time for a coffee break! 🧘‍♂️

---

## 🔍 Example VSS query in DuckDB SQL

```sql
-- Assume we already have an embedding for the query
SELECT 
    title, overview,
    array_cosine_similarity(overview_embeddings, '[query_embedding]') AS score
FROM movies
ORDER BY score DESC
LIMIT 5;
```

---

## 🐍 Python Example

We’ve included a script for this in `utils/vss.py`.

⚠️ **Run it as a module:**

```bash
python -m utils.vss "astronaut adventure" --limit 5 --model mxbai-embed-large
```

This script:
- Generates a query embedding using Ollama
- Computes cosine similarity between query and `overview_embeddings`
- Returns the top matches

---

## 🏎️ Optional: Accelerating Vector Search with DuckDB's `vss` Extension

Once you’ve implemented basic vector similarity search, you can dramatically improve performance by leveraging DuckDB’s experimental `vss` extension.

### 🔔 Why use `vss`?

✅ Avoid full table scans for every query  
✅ Faster approximate nearest neighbor (ANN) retrieval using **HNSW indexes**  
✅ Pure SQL experience—no Python logic required at query time

### 🧰 Steps to enable `vss`

1️⃣ **Install and load the extension:**

```sql
INSTALL 'vss';
LOAD 'vss';
```

2️⃣ **Enable experimental persistence (recommended for this tutorial):**

💡 **Why enable experimental persistence?**

By default, DuckDB allows HNSW indexes only for in-memory databases.

For convenience in this tutorial, we explicitly enable it on disk:

```sql
PRAGMA hnsw_enable_experimental_persistence=true;
CREATE INDEX idx_movies_overview ON movies USING HNSW(overview_embeddings);
```

⚠️ This is experimental behavior—use with caution and avoid in production until fully supported.

3️⃣ **Run accelerated queries:**

```sql
SELECT 
    title, overview,
    array_cosine_distance(overview_embeddings, [query_embedding]) AS score
FROM movies
ORDER BY score ASC
LIMIT 5;
```

### ⚠️ Notes and Caveats

- The `vss` extension is **experimental as of DuckDB 1.0**. Persistence guarantees and stability may evolve in future versions.
- Index creation is an in-memory operation and may consume significant RAM for larger datasets.
- Use this technique **for high-performance scenarios when approximate search is acceptable.**

---

## 🎯 Key Takeaways

- VSS enables **semantic search** beyond keyword matching
- Embeddings capture the *meaning* of text
- Ollama integration makes this easy to run locally

👉 [Next: Hybrid Search ➡️](05_hybrid_search.md)
