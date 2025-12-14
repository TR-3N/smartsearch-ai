import os
import requests
from utils import clean_text, get_embedding, cosine_similarity


class SemanticSearch:
    def __init__(self):
        self.api_key = os.getenv("SERPAPI_KEY")
        if not self.api_key:
            raise ValueError("SERPAPI_KEY not found in environment variables")

    def search(self, query, top_k=5):
        # Call SerpAPI
        params = {
            "q": query,
            "api_key": self.api_key,
            "engine": "google",
            "num": top_k,
        }
        response = requests.get("https://serpapi.com/search", params=params)
        if response.status_code != 200:
            return [{"error": f"API call failed: {response.status_code}"}]

        results = response.json().get("organic_results", [])

        # Compute query embedding
        query_text = clean_text(query)
        query_emb = get_embedding(query_text)

        scored = []
        for item in results:
            title = item.get("title", "")
            snippet = item.get("snippet", "")
            combined = clean_text(f"{title} {snippet}")
            doc_emb = get_embedding(combined)
            score = float(cosine_similarity(query_emb, doc_emb))

            scored.append({
                "name": title or "No Title",
                "description": snippet or "No description available.",
                "link": item.get("link", "#"),
                "score": score,
            })

        # Sort by semantic score (highest first)
        scored.sort(key=lambda x: x["score"], reverse=True)
        return scored


