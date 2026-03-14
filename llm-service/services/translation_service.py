"""
translation_service.py

Handles multilingual responses for the chatbot.
Currently supports simple translations.
"""

from config.settings import SUPPORTED_LANGUAGES


def translate_text(text: str, language: str = "en") -> str:
    """
    Translate chatbot response.

    Args:
        text (str): original response
        language (str): target language

    Returns:
        str: translated text
    """

    language = language.lower()

    if language not in SUPPORTED_LANGUAGES:
        return text

    if language == "hi":
        return "यह अनुवादित उत्तर है: " + text

    if language == "te":
        return "ఇది అనువదించిన సమాధానం: " + text

    return text


def get_supported_languages():
    """
    Return supported language list
    """

    return SUPPORTED_LANGUAGES