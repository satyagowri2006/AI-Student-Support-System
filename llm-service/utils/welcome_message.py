"""
welcome_message.py

Provides chatbot welcome message and suggestions.
"""

def get_welcome_message():

    message = """
Hello 👋

Welcome to the Vignan University Student Support Assistant.

How can I assist you today?
"""

    suggestions = [
        "What courses are available in Vignan University?",
        "What is the hostel fee?",
        "How can I apply for admission?",
        "What scholarships are available?",
        "What are the placement opportunities?"
    ]

    return {
        "message": message,
        "suggestions": suggestions
    }