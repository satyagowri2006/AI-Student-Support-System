from fastapi import APIRouter
from services.chatbot_service import generate_response
from config.database import queries
from datetime import datetime

router = APIRouter()

@router.post("/chatbot")
def chatbot(query: dict):

    question = query["question"]

    answer = generate_response(question)

    data = {
        "question": question,
        "response": answer,
        "timestamp": datetime.now()
    }

    queries.insert_one(data)

    return {"answer": answer}