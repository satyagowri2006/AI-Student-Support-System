"""
helpers.py

Utility helper functions used across the chatbot system.
"""


def clean_text(text: str) -> str:
    """
    Clean user input text
    """

    if not text:
        return ""

    return text.strip().lower()


def validate_query(query: str) -> bool:
    """
    Validate student query input
    """

    if not query:
        return False

    if len(query.strip()) == 0:
        return False

    return True


def format_response(response: str) -> str:
    """
    Format chatbot response
    """

    if not response:
        return "Sorry, I could not understand your question."

    return response.strip().capitalize()


def truncate_text(text: str, max_length: int = 200) -> str:
    """
    Limit response length
    """

    if len(text) <= max_length:
        return text

    return text[:max_length] + "..."