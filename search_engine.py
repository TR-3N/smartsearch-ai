
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pandas as pd

class SemanticSearch:
    def __init__(self, data_path):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.data = pd.read_csv(data_path)
        self.corpus = self.data['description'].tolist()
        self.corpus_embeddings = self.model.encode(self.corpus, convert_to_numpy=True)
        self.index = faiss.IndexFlatL2(self.corpus_embeddings[0].shape[0])
        self.index.add(self.corpus_embeddings)

    def search(self, query, top_k=3):
        query_embedding = self.model.encode([query], convert_to_numpy=True)
        distances, indices = self.index.search(query_embedding, top_k)
        results = []
        for idx in indices[0]:
            results.append({
                'title': self.data.iloc[idx]['title'],
                'description': self.data.iloc[idx]['description']
            })
        return results
