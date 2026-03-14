"""
intent_handler.py

Detects user intent from question.
"""


def detect_intent(query: str):

    query = query.lower().strip()

    admission_keywords = [
        "admission", "apply", "application",
        "eligibility", "vsat"
    ]

    academic_keywords = [
        "course", "courses", "subject",
        "credit", "semester", "branch"
    ]

    financial_keywords = [
        "fee", "fees", "scholarship",
        "loan", "payment", "cost"
    ]

    campus_keywords = [
        "hostel", "transport",
        "bus", "facility", "campus"
    ]

    mental_health_keywords = [
        "stress", "depressed",
        "anxiety", "counseling"
    ]

    if any(word in query for word in admission_keywords):
        return "admission"

    if any(word in query for word in academic_keywords):
        return "academic"

    if any(word in query for word in financial_keywords):
        return "financial"

    if any(word in query for word in campus_keywords):
        return "campus"

    if any(word in query for word in mental_health_keywords):
        return "mental_health"

    return "general"