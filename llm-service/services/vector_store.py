"""
vector_store.py

Builds FAISS vector database and retrieves relevant context.
"""

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

DOCUMENTS = []


def load_documents(file_path):

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    docs = [chunk.strip() for chunk in text.split("\n\n") if chunk.strip()]

    return docs


def build_index(file_path):

    global DOCUMENTS

    DOCUMENTS = load_documents(file_path)

    embeddings = embedding_model.encode(DOCUMENTS)

    embeddings = np.array(embeddings).astype("float32")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    return index


INDEX = build_index("knowledge_base/vignan_data.txt")


def retrieve_context(question, top_k=2):

    question = question.lower().strip()

    query_embedding = embedding_model.encode([question])
    query_embedding = np.array(query_embedding).astype("float32")

    distances, indices = INDEX.search(query_embedding, top_k)

    results = []

    for idx in indices[0]:
        results.append(DOCUMENTS[idx])

    context = "\n".join(results)

    return context