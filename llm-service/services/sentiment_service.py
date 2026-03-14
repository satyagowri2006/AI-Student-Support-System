"""
sentiment_service.py

Basic sentiment analysis for student queries.
Detects whether a message contains negative emotional signals.
"""

from config.settings import NEGATIVE_KEYWORDS


def analyze_sentiment(text: str) -> str:
    """
    Analyze sentiment of a student query.

    Args:
        text (str): student message

    Returns:
        str: sentiment type
            - positive
            - negative
            - neutral
    """

    text = text.lower()

    # Check negative keywords
    for word in NEGATIVE_KEYWORDS:
        if word in text:
            return "negative"

    # simple positive words
    positive_words = [
        "happy",
        "good",
        "great",
        "excited",
        "thank you",
        "thanks"
    ]

    for word in positive_words:
        if word in text:
            return "positive"

    return "neutral"


def is_student_stressed(text: str) -> bool:
    """
    Detect if student might need mental health support
    """

    sentiment = analyze_sentiment(text)

    return sentiment == "negative"