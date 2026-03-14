from utils.faq_suggestions import suggest_questions


def format_response(answer: str):

    if not answer:
        return "I couldn't find that information."

    cleaned = answer.strip()

    suggestions = suggest_questions()

    suggestion_text = "\n\nYou may also ask:\n"

    for q in suggestions:
        suggestion_text += f"- {q}\n"

    return cleaned + suggestion_text