# 🔎 Search Explainer

A hands-on tutorial project that demonstrates modern search paradigms using **DuckDB**, **Ollama embeddings**, and a **developer-friendly Python toolkit**.

This project is designed as a **portfolio-quality reference and a future-ready course framework**.

---

## 📦 Project Structure

```
search_explainer/
├── data/             # Datasets (excluded via .gitignore)
├── utils/            # Modular scripts for DB setup, indexing, embeddings, search
├── docs/             # Markdown tutorials (Setup, Lexical, FTS, VSS, Hybrid)
├── movies.duckdb     # DuckDB database file (excluded via .gitignore)
├── requirements.txt  # Python dependencies
├── .gitignore
├── .gitattributes
└── README.md         # You are here!
```

---

## 🎯 Objectives

✅ Explain core search paradigms:
- Lexical Search
- Full-Text Search (BM25)
- Vector Similarity Search (VSS)
- Hybrid Search with RRF

✅ Provide developer-ready, reproducible examples:
- DuckDB native tooling (`fts`, `vss` extensions)
- Hugging Face + Ollama embeddings
- CLI utilities
- Clean schema & dataset loading

✅ Serve as a future foundation for a **Reflex-based UI demo** and an extensible technical course.

---

## 🏃‍♂️ Quick Start

```bash
# (Optional but recommended) Create a virtual environment
python -m venv venv
source venv/bin/activate   # Linux/macOS
# venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

---

### 🔧 Workflow

```bash
# Download dataset
python -m utils.dataset

# Initialize database and schema
python -m utils.schema

# Create FTS index
python -m utils.fts

# Generate embeddings (requires Ollama running locally)
python -m utils.embeddings

```

---

### 🔍 Example Search Scripts

#### 🔤 Lexical Search
```bash
python -m utils.lexical_search "alien" --limit 10
```

#### 📝 Full-Text Search
```bash
python -m utils.fts_search "space exploration" --limit 5 --fields overview
```

#### 🧠 Vector Similarity Search
```bash
python -m utils.vss "space adventure" --limit 5 --model mxbai-embed-large
```

---

## 📖 Documentation

Tutorials and walkthroughs are in the [`docs/`](docs/index.md) folder:

- [Setup](docs/01_setup.md)
- [Lexical Search](docs/02_lexical_search.md)
- [Full-Text Search](docs/03_full_text_search.md)
- [Vector Similarity Search](docs/04_vector_search.md)
- [Hybrid Search](docs/05_hybrid_search.md)

---

## 🔔 Notes

- Dataset: [TMDB Movie Dataset](https://www.kaggle.com/datasets/israrqayyum11/the-movie-database-tmdb)
- DuckDB extensions: `fts`, `vss`
- Embedding generator: [Ollama](https://ollama.ai/)
- Embedding generation (~8,500 records) may take ~18 minutes on an M1 Mac — ☕ ideal coffee break!

---

## 🧰 Development Standards

- `.gitignore`: Excludes `movies.duckdb`, dataset files, caches, virtualenvs
- `.gitattributes`: Normalizes line endings and enforces file type handling
- Modular, clean Python utilities for easy reuse and composition
- Consistent `python -m utils.*` execution pattern for all scripts

---

✨ **Happy building — and happy searching!** 🚀
