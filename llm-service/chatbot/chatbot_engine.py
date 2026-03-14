"""
chatbot_engine.py

Main orchestration logic for the AI Student Support chatbot.

Pipeline:
Voice/Text Input
        ↓
Language Detection
        ↓
Translate → English
        ↓
Spell Correction
        ↓
Intent Detection
        ↓
RAG Retrieval (FAISS)
        ↓
Prompt Builder
        ↓
LLM Answer Generation
        ↓
Translate → User Language
        ↓
Return Response
"""

from services.vector_store import retrieve_context
from chatbot.intent_handler import detect_intent
from chatbot.memory_manager import add_to_memory, get_memory_context
from utils.spell_corrector import correct_spelling
from utils.translator import detect_language, translate_to_english, translate_from_english
from prompts.prompt_builder import build_prompt
from models.llm_loader import generate_answer
from chatbot.response_generator import format_response


def process_query(user_query: str):

    try:

        # 1️⃣ Detect user language
        language = detect_language(user_query)

        print("Detected language:", language)

        # 2️⃣ Translate query to English
        english_query = translate_to_english(user_query)

        # 3️⃣ Normalize and spell correction
        english_query = correct_spelling(
            english_query.lower().strip()
        )

        # 4️⃣ Detect intent
        intent = detect_intent(english_query)

        # 5️⃣ Retrieve context from FAISS
        context = retrieve_context(english_query)

        # 6️⃣ Load conversation memory
        memory_context = get_memory_context()

        full_context = memory_context + "\n" + context

        # 7️⃣ Build prompt
        prompt = build_prompt(full_context, english_query)

        # 8️⃣ Generate answer using LLM
        answer = generate_answer(prompt)

        # 9️⃣ Clean response
        response = format_response(answer).strip()

        # 🔟 Translate response back to user language
        final_response = translate_from_english(response, language)

        # 1️⃣1️⃣ Save conversation
        add_to_memory("Student", english_query)
        add_to_memory("Bot", final_response)

        # return response + language (for voice chatbot)
        return final_response, language

    except Exception as e:

        print("Chatbot error:", str(e))

        return "Sorry, I encountered an issue while processing your request.", "en"