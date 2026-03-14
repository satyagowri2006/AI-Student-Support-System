"""
memory_manager.py

Stores previous conversation messages.
"""

conversation_memory = []


def add_to_memory(role, message):

    conversation_memory.append({
        "role": role,
        "message": message
    })

    # keep only last 5 messages
    if len(conversation_memory) > 5:
        conversation_memory.pop(0)


def get_memory_context():

    context = ""

    for item in conversation_memory:
        context += f"{item['role']}: {item['message']}\n"

    return context