# 🔗 Hybrid Search with Reciprocal Rank Fusion (RRF)

## 🚀 Example Scenario

Suppose we want to **combine the strengths of lexical, full-text, and vector search**:  
- Lexical search handles exact keyword matches  
- Full-text search ranks by BM25 relevance  
- Vector search brings semantic understanding

🔔 **Hybrid search blends these signals for better retrieval quality.**

---

## 🧠 What is Reciprocal Rank Fusion (RRF)?

RRF is a simple but effective algorithm that **merges ranked result lists** from different search paradigms.

For each result `d` in list `Lᵢ` at position `rankᵢ(d)`, its RRF score is:

```
RRF(d) = Σ 1 / (k + rankᵢ(d))
```

Where `k` is a tunable constant (commonly `k=60`).

---

## 🛠️ Approach in this project

While DuckDB doesn’t have a native RRF implementation, we can:

1️⃣ Retrieve ranked lists from:
- Lexical search (`utils.lexical_search.py`)
- Full-text search (`utils.fts_search.py`)
- Vector similarity search (`utils.vss.py`)

2️⃣ Fuse the results in Python (e.g., using pandas or custom logic).

---

## 🐍 Example Workflow

⚠️ **Example hybrid search script (conceptual — implementation suggested as an exercise for readers):**

```bash
python -m utils.hybrid_search "alien adventure" --limit 10 --rrf_k 60
```

This would:
- Run all three search types
- Merge their ranked results using RRF
- Output top-N results with combined relevance scores

---

## 🎯 Key Takeaways

- Hybrid search improves retrieval coverage and ranking robustness  
- RRF is simple to implement and works with any set of ranked lists  
- A great tool when combining lexical + semantic signals

---

👉 Congratulations — you’ve now completed the **Search Explainer Tutorial Series**! 🎉

✨ Bonus exercise: Implement `utils/hybrid_search.py` using DuckDB queries + Python RRF merge logic.
