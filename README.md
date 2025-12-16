# 🔍 SmartSearchAI

SmartSearchAI is a **live semantic search engine** that lets users ask natural language questions and retrieves intelligent answers sourced directly from the internet — **no static dataset required**.

It uses:
- 🌐 [SerpAPI](https://serpapi.com/) to fetch real-time Google Search results
- 🤖 [SentenceTransformers](https://www.sbert.net/) to embed queries and result snippets
- 🧠 Cosine similarity to rerank results by **semantic closeness**, not just keyword overlap
- 🖥️ [Streamlit](https://streamlit.io/) for an intuitive web interface
- 🌐 [Flask](https://flask.palletsprojects.com/) to expose a simple `/search` JSON API

---

## ✨ Features

- 🔎 Real-time web search via SerpAPI (Google Search API)  
- 🧠 Semantic reranking of results using SentenceTransformer embeddings and cosine similarity  
- 🧩 Clean separation of concerns:
  - `Flask` backend: `/search` endpoint returning JSON
  - `Streamlit` frontend: user UI calling the backend
- 📄 Modern web UI with sidebar navigation and custom styling  
- 🔐 API key loaded securely from `.env` (not committed)

---

## 📸 Demo Idea

For demo, try queries where semantics matter more than exact wording, for example:

- “cheap ways to exercise at home” vs “low-cost home workout ideas”  
- “how to fix python environment not found” vs “python venv activation error in powershell”  

You can highlight that top results stay relevant even when keywords don’t match exactly, because ranking is based on embedding similarity.

---

## 🚀 Getting Started

### 1. Clone the repo

```
git clone https://github.com/TR-3N/smartsearch-ai.git
cd smartsearch-ai
```

> If you’re using a different remote or fork, adjust the URL accordingly.

### 2. Create and activate a virtual environment

```
python -m venv smartsearch_env
```

On **Windows (PowerShell)**:

```
# If needed, allow scripts just for this session:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

.\smartsearch_env\Scripts\Activate.ps1
```

On **Windows (cmd.exe)**:

```
smartsearch_env\Scripts\activate.bat
```

On **macOS / Linux**:

```
source smartsearch_env/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
pip install sentence-transformers streamlit-extras streamlit-option-menu
```

`requirements.txt` covers the core stack (Streamlit, Flask, CORS, dotenv, requests, etc.), and `sentence-transformers` plus the Streamlit extras are installed explicitly. [file:2][file:4][file:6]

---

## 🔑 SerpAPI Setup

1. Go to https://serpapi.com/ and sign up (free plan available).  
2. Get your SerpAPI key.  
3. Create a `.env` file in the project root:

```
SERPAPI_KEY=your_serpapi_key_here
```

> Important: `.env` is listed in `.gitignore` and **must not** be committed.

The backend reads `SERPAPI_KEY` in `search_engine.py` and will throw a clear error if it is missing. [file:3][file:5]

---

## 🧪 Running the App (Backend + Frontend)

The app runs as two processes: a Flask API and a Streamlit UI.

### 1. Start the Flask semantic backend

In a terminal with the virtualenv activated:

```
python app.py
```

This starts Flask at `http://127.0.0.1:5000` and exposes:

- `POST /search` — accepts JSON `{"query": "...", "top_k": 5}` and returns a list of result objects with semantic `score`. [file:3][file:7]

Leave this terminal running.

### 2. Start the Streamlit frontend

Open a **second** terminal, activate the same virtualenv, `cd` into the project folder, then run:

```
streamlit run streamlit_app.py
```

Open `http://localhost:8501` in your browser.

- Use the **Home** page to enter a natural language query.  
- Streamlit calls the Flask `/search` endpoint, which:
  - Calls SerpAPI to fetch organic Google results. [file:3]  
  - Computes embeddings for the query and each result (`title + snippet`) using `all-MiniLM-L6-v2`. [file:4]  
  - Computes cosine similarity and sorts results by semantic `score`. [file:3][file:4]  
- The UI displays the top results with title, description, link, and (optionally) the semantic score. [file:6]

---

## 🧠 How the Semantic Ranking Works

Inside `search_engine.py`, the `SemanticSearch` class:

1. Reads `SERPAPI_KEY` from environment variables. [file:3]  
2. Calls `https://serpapi.com/search` with the user query and retrieves `organic_results`. [file:3]  
3. For each result, builds a text string from `title` and `snippet` and passes it to `utils.py`. [file:3][file:4]  
4. `utils.py`:
   - Loads the `all-MiniLM-L6-v2` SentenceTransformer model.  
   - Provides:
     - `clean_text(text)` – basic normalization
     - `get_embedding(text)` – returns a dense embedding
     - `cosine_similarity(a, b)` – similarity between query and result embeddings. [file:4]
5. Results are scored by cosine similarity, sorted descending, and returned to Streamlit. [file:3][file:4]

This makes SmartSearchAI behave differently from a classic keyword engine: it can understand paraphrases and re-order SerpAPI’s results based on **meaning** rather than position alone. [file:3][file:4][file:5]

---

## 📁 Project Structure

```
.
├── app.py               # Flask API: /search endpoint
├── search_engine.py     # SemanticSearch class (SerpAPI + embeddings)
├── streamlit_app.py     # Streamlit UI
├── utils.py             # SentenceTransformer model + helpers
├── requirements.txt     # Core Python dependencies
├── .env                 # Contains SERPAPI_KEY (not committed)
├── .gitignore
└── README.md
```

---

## 📌 Future Improvements

Some ideas you can implement next:

- Add OpenAI / GPT (or another LLM) to **summarize** the top results into one concise answer. [file:2][file:5]  
- Show both “Original Google rank” and “Semantic rank” side-by-side in the UI for demo purposes.  
- Cache SerpAPI responses and embeddings to speed up repeated queries. [file:5]

---

## 🛡️ License

This project is open-source and available under the MIT License. [file:5]

---

## 🙋‍♂️ Author

**Shahil Sinha**

Feel free to reach out on LinkedIn or open issues / PRs on this repo if you want to contribute or suggest improvements! [file:5]
```
