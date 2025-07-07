# 📚 Search Explainer - Tutorial Series

## 🎯 Objectives
- Explain core search paradigms in modern data systems.
- Cover full text search, vector search, and semantic search with hands-on examples and code walkthroughs.
- Bridge foundational search theory with applied tools like Hugging Face embeddings and DuckDB.
- Serve as a developer-friendly guide for search system architecture and performance insights.

---

## 🧭 Table of Contents

### 1. 🚀 Setup
- [Install `duckdb`, `reflex`](./install_dependencies.md)
- Load sample dataset (e.g., documents, product catalog, articles)

### 2. 🔤 Lexical Search
- What is lexical search?
- How does it work (string matching, tokenization)?
- Implement basic search UI using Reflex

### 3. 📚 Full Text Search
- What is full text search?
- How does it differ from lexical search?
- Install and use `fts` extension in DuckDB
- Create full text index and run queries
- Update UI to allow switching between lexical and FTS

### 4. 🧠 Vector Similarity Search
- What is vector similarity search?
- How does it work (embeddings, cosine similarity)?
- Install and use `vss` extension in DuckDB
- Generate vectors using Hugging Face embeddings
- Update UI to allow vector-based search

### 5. 🌀 Hybrid Search
- What is hybrid search?
- What is Reciprocal Rank Fusion (RRF)?
- Install and use `flockmtl` (or similar tool)
- Combine FTS and vector results with RRF
- Update UI to support hybrid search selection

---

Stay tuned for code examples, diagrams, and interactive search playgrounds!
