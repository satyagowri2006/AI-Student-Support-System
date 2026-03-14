"""
knowledge_retriever.py
Simple retrieval from knowledge base text file.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
KB_FILE = os.path.join(BASE_DIR, "knowledge_base", "vignan_data.txt")


def retrieve_context(question: str, intent: str = "general") -> str:
    """
    Returns knowledge base content.
    Future improvement: semantic search.
    """

    try:
        with open(KB_FILE, "r", encoding="utf-8") as f:
            data = f.read()
    except FileNotFoundError:
        data = "Knowledge base unavailable."

    return data