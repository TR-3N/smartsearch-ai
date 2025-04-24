# 🔍 SmartSearchAI

SmartSearchAI is a semantic search engine powered by **SentenceTransformers** and **Streamlit**. It allows users to search through climate change-related information using natural language queries. By utilizing **semantic search**, the app finds the most relevant information based on the meaning of the query—not just keyword matches.

---

## 🚀 Features

- 🔍 **Semantic Search** using BERT-based embeddings.
- 🧠 **Natural Language Query Support**.
- 📂 **Custom Dataset Support** – plug in your own CSV.
- 💻 **Streamlit UI** – clean, responsive, and interactive.
- ☁️ **Easily Deployable** – works on any platform with minimal setup.

---

## 📂 Project Structure

smartsearch-ai/ ├── app.py # Streamlit app entry point ├── search_engine.py # Core logic for semantic search ├── utils.py # Text cleaning and preprocessing ├── data/ │ └── climate_data.csv # Custom dataset ├── requirements.txt # Python dependencies └── README.md # You're reading it!

yaml
Copy code

---

## 📊 Dataset

The app uses a dataset stored in `data/climate_data.csv`, with the following structure:

| id | title               | description                                               |
|----|---------------------|-----------------------------------------------------------|
| 1  | Climate Change...   | Rising sea levels, acidification, and warming...          |
| 2  | Deforestation       | Loss of forests increases CO₂, contributing to climate...|
| 3  | Renewable Energy    | Wind and solar reduce carbon emissions...                |

---

## 🛠️ Installation

Follow these steps to run the app locally:

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/smartsearch-ai.git
cd smartsearch-ai
Create a virtual environment:

bash
Copy code
python -m venv smartsearch_env
Activate the environment:

On Windows:

bash
Copy code
.\smartsearch_env\Scripts\activate
On macOS/Linux:

bash
Copy code
source smartsearch_env/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the app:

bash
Copy code
streamlit run app.py
🧪 Example Queries
“What are the effects of rising sea levels?”

“How does deforestation affect the environment?”

“What are the benefits of renewable energy?”

⚙️ How It Works
Dataset Loading: SemanticSearch loads the CSV and merges the title + description.

Text Embedding: Converts text into vectors using SentenceTransformer.

Query Embedding: Same model encodes the user's query.

Similarity Search: Uses cosine similarity with FAISS to retrieve top results.

Display: Streamlit shows the results interactively.

🧾 Dependencies
streamlit

pandas

scikit-learn

sentence-transformers

faiss-cpu

📈 To Do / Future Enhancements
 Add category/date filters

 Support multiple datasets

 GPT-powered answer summarization

 Public deployment on Streamlit Cloud or Heroku

📢 Contributing
Fork the repo, create a branch, and open a pull request. Suggestions and issues are welcome!

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

🏷️ Tags
#AI #MachineLearning #SemanticSearch #NLP #Streamlit #ClimateChange #DataScience