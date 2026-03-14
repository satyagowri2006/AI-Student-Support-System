"""
translator.py

Language detection and translation utilities.
Supports Telugu, Hindi, and English.
"""

from deep_translator import GoogleTranslator
from langdetect import detect


def detect_language(text):
    """
    Detect language of the input text.
    """

    try:
        lang = detect(text)
        return lang
    except:
        return "en"


def translate_to_english(text):
    """
    Translate Telugu/Hindi/other language → English
    """

    try:
        translated = GoogleTranslator(
            source="auto",
            target="en"
        ).translate(text)

        return translated

    except:
        return text


def translate_from_english(text, target_lang):
    """
    Translate English response back to user's language.
    """

    if target_lang == "en":
        return text

    try:
        translated = GoogleTranslator(
            source="en",
            target=target_lang
        ).translate(text)

        return translated

    except:
        return text