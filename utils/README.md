# 🔧 `utils/` Directory README

This `utils/` directory contains modular, reusable utility scripts to support the **Search Explainer Tutorial Series**. These scripts enable you to download datasets, prepare your database, generate embeddings, create search indexes, and run search queries.

## 📦 Utilities Overview

### 1️⃣ **`dataset.py`**  
Download and extract the TMDB dataset from KaggleHub.
```bash
python utils/dataset.py
```

### 2️⃣ **`schema.py`**  
Initialize the DuckDB database, load the dataset as the `movies` table, and ensure embedding columns are present.
```bash
python utils/schema.py
```

### 3️⃣ **`fts.py`**  
Install DuckDB FTS extension and create a full-text search index.
```bash
python utils/fts.py
```

### 4️⃣ **`fts_search.py`**  
Perform a full-text BM25 search.
```bash
python utils/fts_search.py "adventure" --limit 5 --fields overview
```

### 5️⃣ **`embeddings.py`**  
Pull Ollama embedding model (if not present) and generate/store embeddings for movie titles and overviews.
```bash
python utils/embeddings.py --model mxbai-embed-large --batch_size 100
```

### 6️⃣ **`vss.py`**  
Perform a vector similarity search using Ollama embeddings.
```bash
python utils/vss.py "space adventure" --model mxbai-embed-large --limit 5
```

## 🛠️ Common Workflow

1️⃣ **Download dataset:**  
`python utils/dataset.py`

2️⃣ **Load and initialize DB:**  
`python utils/schema.py`

3️⃣ **Add embeddings:**  
`python utils/embeddings.py`

4️⃣ **Create FTS index:**  
`python utils/fts.py`

5️⃣ **Search examples:**  
- Full-text: `python utils/fts_search.py "alien"`  
- Vector: `python utils/vss.py "alien adventure"`

## 🔒 Notes
- **DuckDB file:** `movies.duckdb` in project root.
- **Dataset file:** `data/moviesData.csv`.
- **Model dependency:** Requires [Ollama](https://ollama.ai/) running locally for embedding generation and inference.

---

✨ Ready to plug these utilities into your tutorial series or future Reflex UI. Enjoy! 🎯
