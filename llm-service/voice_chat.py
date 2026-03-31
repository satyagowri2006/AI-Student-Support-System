"""
voice_chat.py

Voice chatbot interface
"""

from voice.voice_service import listen_to_user, speak_response
from chatbot.chatbot_engine import process_query


def start_voice_chat():

    print("Voice chatbot started. Say 'exit' to stop.")

    while True:

        # 🎤 Listen to user
        user_query = listen_to_user()

        if not user_query:
            continue

        if user_query.lower() == "exit":
            speak_response("Goodbye", "en")
            break

        # 🧠 Process query using chatbot engine
        answer, language = process_query(user_query)

        print("Bot:", answer)

        # 🔊 Speak response in correct language
        speak_response(answer, language)


if __name__ == "__main__":

    start_voice_chat()