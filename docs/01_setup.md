## 🚀 Setup

### 🐍 (Optional but Recommended) Create a Virtual Environment

We recommend using a virtual environment to isolate project dependencies:

```bash
# Create virtual environment
python -m venv venv

# Activate on Linux/macOS
source venv/bin/activate

# Activate on Windows
venv\Scripts\activate
```

---

### 📁 Install Dependencies

Create a `requirements.txt` file with the following:

```
duckdb
duckdb-engine
reflex
pandas
huggingface-hub
sentence-transformers
kagglehub
ollama
```

Then install using pip:

```bash
pip install -r requirements.txt
```

💡 Already using `conda`, `poetry`, or your own environment manager? Feel free to manage your environment your way.

---

👉 [Next: Lexical Search ➡️](02_lexical_search.md)