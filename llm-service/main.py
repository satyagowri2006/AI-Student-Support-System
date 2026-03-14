from fastapi import FastAPI
from pydantic import BaseModel
from chatbot.chatbot_engine import process_query

app = FastAPI()


class Question(BaseModel):
    question: str
    language: str = "en"


@app.post("/ask")
def ask_question(q: Question):

    answer = process_query(q.question, q.language)

    return {"answer": answer}


if __name__ == "__main__":

    print("AI Student Support Chatbot")
    print("Type 'exit' to stop\n")

    while True:

        query = input("Student: ")

        if query.lower() == "exit":
            print("Chatbot stopped.")
            break

        response = process_query(query)

        print("Bot:", response)