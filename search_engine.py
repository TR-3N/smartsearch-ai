import os
import requests

class SemanticSearch:
    def __init__(self):
        self.api_key = os.getenv("SERPAPI_KEY")
        if not self.api_key:
            raise ValueError("SERPAPI_KEY not found in environment variables")

    def search(self, query, top_k=5):
        params = {
            "q": query,
            "api_key": self.api_key,
            "engine": "google",
            "num": top_k
        }

        response = requests.get("https://serpapi.com/search", params=params)

        if response.status_code != 200:
            return [{"error": f"API call failed: {response.status_code}"}]

        results = response.json().get("organic_results", [])
        formatted = [{
            "name": item.get("title", "No Title"),
            "description": item.get("snippet", "No description available."),
            "link": item.get("link", "#"),
            "score": 1.0
        } for item in results]

        return formatted
