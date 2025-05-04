from flask import Flask, request, jsonify
from flask_cors import CORS
from search_engine import SemanticSearch
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

semantic_search = SemanticSearch()

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    query = data.get("query")
    top_k = data.get("top_k", 5)
    results = semantic_search.search(query, top_k=top_k)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
