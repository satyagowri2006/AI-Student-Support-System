import requests
from bs4 import BeautifulSoup
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

urls = [
    "https://vignan.ac.in/",
    "https://vignan.ac.in/admissions.php",
    "https://vignan.ac.in/program.php",
    "https://vignan.ac.in/placements.php",
    "https://vignan.ac.in/facilities.php"
]

documents = []


def scrape_page(url):

    try:
        response = requests.get(url, timeout=10)

        soup = BeautifulSoup(response.text, "html.parser")

        paragraphs = soup.find_all("p")

        text = " ".join([p.get_text() for p in paragraphs])

        return text

    except:
        return ""


def collect_documents():

    global documents

    for url in urls:
        if "vignan.ac.in" not in url:
            continue

        text = scrape_page(url)

        chunks = [text[i:i+500] for i in range(0, len(text), 500)]

        documents.extend(chunks)

    return documents


def build_vector_database():

    docs = collect_documents()

    embeddings = embedding_model.encode(docs)

    embeddings = np.array(embeddings).astype("float32")

    dim = embeddings.shape[1]

    index = faiss.IndexFlatL2(dim)

    index.add(embeddings)

    faiss.write_index(index, "knowledge_base/vignan_index.faiss")

    return index, docs


if __name__ == "__main__":

    print("Collecting website data...")

    index, docs = build_vector_database()

    print("Documents indexed:", len(docs))

    print("Vector database created successfully.")