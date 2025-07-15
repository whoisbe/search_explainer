# 🔧 `utils/` Directory README

This `utils/` directory contains modular, reusable utility scripts to support the **Search Explainer Tutorial Series**. These scripts enable you to download datasets, prepare your database, generate embeddings, create search indexes, and run search queries.

## 📦 Utilities Overview

### 1️⃣ `dataset.py`  
Download and extract the TMDB dataset from KaggleHub:
```bash
python -m utils.dataset
```

### 2️⃣ `schema.py`  
Initialize the DuckDB database, load the dataset as the `movies` table, and ensure embedding columns are present:
```bash
python -m utils.schema
```

### 3️⃣ `fts.py`  
Install DuckDB FTS extension and create a full-text search index:
```bash
python -m utils.fts
```

### 4️⃣ `fts_search.py`  
Perform a full-text BM25 search:
```bash
python -m utils.fts_search "adventure" --limit 5 --fields overview
```

### 5️⃣ `embeddings.py`  
Pull Ollama embedding model (if not present) and generate/store embeddings for movie titles and overviews:
```bash
python -m utils.embeddings --model mxbai-embed-large --batch_size 100
```

### 6️⃣ `lexical_search.py`  
Perform a simple lexical search (case-insensitive substring match):
```bash
python -m utils.lexical_search "alien" --limit 10
```

### 7️⃣ `vss.py`  
Perform a vector similarity search using Ollama embeddings:
```bash
python -m utils.vss "space adventure" --model mxbai-embed-large --limit 5
```

## 🛠️ Common Workflow

1️⃣ **Download dataset:**  
```bash
python -m utils.dataset
```

2️⃣ **Load and initialize DB:**  
```bash
python -m utils.schema
```

3️⃣ **Generate embeddings:**  
```bash
python -m utils.embeddings
```

4️⃣ **Create FTS index:**  
```bash
python -m utils.fts
```

5️⃣ **Example search scripts:**  
- Lexical search:
  ```bash
  python -m utils.lexical_search "alien" --limit 10
  ```

- Full-text search:
  ```bash
  python -m utils.fts_search "alien" --limit 5 --fields overview
  ```

- Vector similarity search:
  ```bash
  python -m utils.vss "alien adventure" --model mxbai-embed-large --limit 5
  ```

## 🔒 Notes
- **DuckDB file:** `movies.duckdb` in project root  
- **Dataset file:** `data/moviesData.csv`  
- **Model dependency:** Requires [Ollama](https://ollama.ai/) running locally for embedding generation and inference  
- ⚠️ Generating embeddings for ~8,500 records may take ~18 minutes on an M1 Mac — ☕ ideal coffee break!

---

✨ Ready to plug these utilities into your tutorial series or future Reflex UI. Enjoy! 🎯
