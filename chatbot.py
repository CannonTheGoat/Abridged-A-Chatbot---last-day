import nltk
from nltk.chat.util import Chat, reflections
pairs = [
    [
        r"my name is (,*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there",]
    ],
    [
        r"Who's the goat",
        ["LeBron Raymone James Sr no question",]
    ],
    [
        r"What's your favorite video game?",
        ["Fortnite",]
    ],
    [
        r"Me or the PS5",
        ["The PS5",]
    ],
    [
        r"quit",
        ["Goodbye! Have a nice day!"]
    ]
]

Chatbot = Chat(pairs, reflections)

def chat():
    print("Hello, I am your chatbot. How can I assist you today?")
    while True:
        user_input = input("Ymou: ")
        if user_input.lower() == "quit":
            print("Goodbye! Have a nice day!")
            break
        else:
            responce = Chatbot.respond(user_input)
            if responce:
                print("Bot", responce)
            else:
                print("Bot: I'm not sure how to respond to that.")

chat()