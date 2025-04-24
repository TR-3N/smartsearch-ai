import streamlit as st
from search_engine import SemanticSearch
from utils import clean_text
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

st.set_page_config(page_title="SmartSearchAI", layout="wide")
st.title("🔍 SmartSearchAI")

# Initialize Sentence-Transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load your dataset (CSV)
data = pd.read_csv("data/climate_data.csv")  # Update path as necessary

# Assuming your CSV has 'title' and 'description' columns (you can modify as needed)
corpus = data[['title', 'description']].apply(lambda x: f"{x['title']} {x['description']}", axis=1).tolist()

# Function for semantic search
def semantic_search(query, corpus):
    query_embedding = model.encode([query])
    corpus_embeddings = model.encode(corpus)
    
    # Calculate cosine similarity between query and all documents
    similarities = cosine_similarity(query_embedding, corpus_embeddings)
    return similarities

search_engine = SemanticSearch("data/climate_data.csv")
  # Adjust if necessary

query = st.text_input("Enter your search query:")

if query:
    st.subheader("Search Results")
    
    cleaned_query = clean_text(query)
    
    # Get the search results using semantic search
    results = semantic_search(cleaned_query, corpus)
    
    # Display top results (you can change the number to show more results)
    top_results = results[0].argsort()[-5:][::-1]  # Get top 5 results
    
    for idx in top_results:
        st.markdown(f"**{data.iloc[idx]['title']}**")
        st.markdown(f"> {data.iloc[idx]['description']}")
        st.markdown("---")

