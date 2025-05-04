import os
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

df = pd.read_csv("data/ai_tools_dataset.csv")

embeddings = model.encode(df["Description"].fillna("").tolist())

os.makedirs("data/embeddings", exist_ok=True)
np.save("data/embeddings/tool_embeddings.npy", embeddings)
