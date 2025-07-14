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
# Install dependencies
pip install -r requirements.txt

# Download dataset
python utils/dataset.py

# Initialize database
python utils/schema.py

# Optional: Add embeddings (requires Ollama running locally)
python utils/embeddings.py

# Create FTS index
python utils/fts.py

# Run lexical search example
python utils/fts_search.py "alien"

# Run vector similarity search example
python utils/vss.py "space adventure"
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

---

## 🧰 Development Standards

- `.gitignore`: Excludes `movies.duckdb`, dataset files, caches, virtualenvs
- `.gitattributes`: Normalizes line endings and enforces file type handling
- Modular, clean Python utilities for easy reuse and composition

---

✨ **Happy building — and happy searching!** 🚀
