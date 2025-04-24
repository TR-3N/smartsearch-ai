# 🔍 SmartSearchAI

SmartSearchAI is a semantic search engine powered by **SentenceTransformers** and **Streamlit**. It allows users to search through climate change-related information using natural language queries. By utilizing **semantic search**, the app finds the most relevant information based on the meaning of the query, not just keyword matches.

---

## 🚀 Features
- **Semantic Search**: Powered by BERT-based models for understanding natural language queries.
- **Custom Dataset Support**: Easily replace the dataset to search on other topics (e.g., job listings, tech articles, etc.)
- **Streamlit UI**: A clean and interactive web interface for users to input queries and view results.
- **Scalable**: Easily deployable on any platform with minimal setup.

---

## 📂 Project Structure

smartsearch-ai/ ├── app.py # Streamlit app entry point ├── search_engine.py # Core logic for semantic search using embeddings ├── utils.py # Text cleaning and preprocessing functions ├── data/climate_data.csv # Dataset containing climate change-related information ├── requirements.txt # Dependencies for the app └── README.md # This file

yaml
Copy code

---

## 📊 Dataset

The app uses a custom dataset stored in `data/climate_data.csv`, which includes climate change-related articles. The dataset has the following columns:

- `id`: Unique identifier for each entry.
- `title`: The title of the article.
- `description`: A short description or summary of the article.

### Sample Data:
```csv
id,title,description
1,"Climate Change and Oceans","Rising sea levels, acidification, and warming disrupt ecosystems."
2,"Deforestation","Loss of forests increases CO₂, contributing to climate change."
3,"Renewable Energy","Wind and solar reduce carbon emissions and dependence on fossil fuels."
🛠️ Installation
Follow the steps below to run SmartSearchAI on your local machine:

1. Clone the repository:
bash
Copy code
git clone https://github.com/your-username/smartsearch-ai.git
cd smartsearch-ai
2. Create a virtual environment:
bash
Copy code
python -m venv smartsearch_env
3. Activate the virtual environment:
For Windows:

bash
Copy code
.\smartsearch_env\Scripts\activate
For macOS/Linux:

bash
Copy code
source smartsearch_env/bin/activate
4. Install dependencies:
bash
Copy code
pip install -r requirements.txt
5. Run the Streamlit app:
bash
Copy code
streamlit run app.py
This will open the app in your browser where you can enter queries and get search results.

🧪 Example Search Queries
Try out some of these queries:

“What are the effects of rising sea levels?”

“How does deforestation affect the environment?”

“What are the benefits of renewable energy?”

📈 How It Works
Dataset Loading: The SemanticSearch class loads the dataset from data/climate_data.csv and combines the title and description columns.

Text Embedding: Using the SentenceTransformer model, the titles and descriptions are converted into embeddings (numerical representations).

Query Embedding: When a user enters a query, it's also converted into an embedding.

Similarity Calculation: Cosine similarity is used to find the most relevant results by comparing the query embedding with the embeddings of the dataset.

Displaying Results: The most relevant results are displayed in the Streamlit UI.

🔧 Dependencies
streamlit: Framework for creating interactive web apps.

pandas: For handling and manipulating the dataset.

scikit-learn: For calculating cosine similarity.

sentence-transformers: For embedding text using pre-trained models.

faiss-cpu: For fast similarity search in large datasets.

⚙️ To Do / Future Improvements
Add more datasets (e.g., job listings, news articles).

Implement advanced search filters (e.g., by date, category).

Integrate GPT for summarization or question answering based on the results.

Deploy the app on platforms like Heroku or Streamlit Cloud for public access.

📢 Contributing
Feel free to fork this repository and contribute! Create issues or pull requests to suggest improvements or new features.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

🏷️ Tags
#AI #MachineLearning #NaturalLanguageProcessing #Streamlit #SemanticSearch #ClimateChange #DataScience