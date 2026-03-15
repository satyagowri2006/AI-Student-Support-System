from predict import get_response

print("AI Student Support Chatbot")

while True:

    message = input("You: ")

    if message.lower() == "quit":
        break

    response = get_response(message)

    print("Bot:",response)