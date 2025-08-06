def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input in ["hi", "hello", "hey"]:
        return "Hello! How can I help you?"
    elif "your name" in user_input:
        return "I am a simple Python chatbot."
    elif "how are you" in user_input:
        return "I'm just code, but I'm doing fine. Thanks!"
    elif "what do you do" in user_input:
        return "I answer basic questions using simple logic."
    elif "location" in user_input or "city" in user_input:
        return "I'm virtual, I live on your computer!"
    elif "created you" in user_input:
        return "I was created by a Python programmer."
    elif user_input in ["bye", "exit", "quit"]:
        return "Goodbye! Have a great day."
    else:
        return "Sorry, I didn't understand that. Try asking something else."


def start_chat():
    print("Hi, I’m your chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("> ")
        response = chatbot_response(user_input)
        print(response)
        if user_input.lower() in ["bye", "exit", "quit"]:
            break


if __name__ == "__main__":
    start_chat()
