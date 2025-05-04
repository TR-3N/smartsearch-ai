# 🔍 SmartSearchAI

SmartSearchAI is a **live semantic search engine** that lets users ask natural language questions and retrieves intelligent answers sourced directly from the internet — **no static dataset required**.

It uses:
- 🌐 [SerpAPI](https://serpapi.com/) to fetch real-time web results
- 🤖 [SentenceTransformers](https://www.sbert.net/) to embed and understand natural language
- ⚡ [FAISS](https://github.com/facebookresearch/faiss) for fast similarity search
- 🖥️ [Streamlit](https://streamlit.io/) for an intuitive web interface

---

## ✨ Features

- 🔎 Real-time search via SerpAPI (Google Search API)
- 🧠 Semantic understanding of user queries (not just keyword matching)
- ⚡ Fast similarity matching using FAISS
- 📄 Clean, responsive web UI built with Streamlit
- 🔐 API key stored securely via `.env` file

---

## 📸 Demo Screenshot

> *(Insert a screenshot here of your Streamlit UI if you have one)*

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/smartsearchai.git
cd smartsearchai
2. Create and Activate a Virtual Environment
bash
Copy code
python -m venv smartsearch_env
smartsearch_env\Scripts\activate   # On Windows
# OR
source smartsearch_env/bin/activate  # On Mac/Linux
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
🔑 SerpAPI Setup
Go to https://serpapi.com/ and sign up (free plan available).

Get your API key.

Create a .env file in the root of the project:

env
Copy code
SERPAPI_API_KEY=your_serpapi_key_here
✅ Important: Never push your .env file to GitHub. It is ignored via .gitignore.

🧪 Run the App
bash
Copy code
streamlit run streamlit_app.py
Then open http://localhost:8501 in your browser.

🧠 How It Works
User enters a natural language question.

App fetches real-time web results from SerpAPI.

Text from results is embedded using a SentenceTransformer model.

FAISS indexes and finds the most semantically similar snippet to the query.

The best match is returned and shown to the user.

📁 Project Structure
bash
Copy code
.
├── app.py
├── generate_embeddings.py
├── search_engine.py
├── streamlit_app.py
├── utils.py
├── requirements.txt
├── .env              # contains SerpAPI key (not committed)
├── .gitignore
└── README.md
📌 To-Do
 Add OpenAI/GPT summarization of results (optional)

 Add multi-page result interface

 Cache frequent queries

🛡️ License
This project is open-source and available under the MIT License.

🙋‍♂️ Author
Shahil Sinha

Feel free to reach out on LinkedIn or contribute to this repo!