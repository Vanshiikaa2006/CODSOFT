import random

print("Welcome to CodSoftBot!")
user_name = input("Bot: Hi there! What's your name?\nYou: ").strip().title()
print(f"Bot: Nice to meet you, {user_name}! You can talk to me. Type 'bye' to end the chat.\n")

greetings = [ 
    f"Hello, {user_name}! How can I help you today?",
    f"Hi {user_name}, what’s up?",
    f"Hey {user_name}! How are you feeling today?"
]

how_are_you_responses = [
    "I'm just a bunch of Python code, but I'm doing great! 😄",
    "I'm feeling code-tastic! How about you?",
    "I don't have feelings, but chatting with you makes my day!"
]

help_responses = [
    "I can chat with you, answer simple questions, and keep you company.",
    "I'm here to talk, answer questions, or just listen. What would you like to do?",
    "Feel free to ask me anything or just tell me about your day!"
]

while True:
    user_input = input(f"{user_name}: ").lower()

    if any(greet in user_input for greet in ["hello", "hi", "hey"]):
        print("Bot:", random.choice(greetings))
    elif "how are you" in user_input:
        print("Bot:", random.choice(how_are_you_responses))
    elif "your name" in user_input:
        print("Bot: I'm CodSoftBot, your friendly chatbot assistant.")
    elif "what can you do" in user_input or "help" in user_input:
        print("Bot:", random.choice(help_responses))
    elif "who made you" in user_input:
        print("Bot: I was created by a CodSoft intern as part of an AI internship task.")
    elif "thank" in user_input:
        print(f"Bot: You're welcome, {user_name}! 😊")
    elif "sad" in user_input or "upset" in user_input:
        print(f"Bot: I'm sorry to hear that, {user_name}. Want to talk about it?")
    elif "happy" in user_input or "excited" in user_input:
        print(f"Bot: That's wonderful, {user_name}! Tell me more!")
    elif "bye" in user_input or "goodbye" in user_input:
        print(f"Bot: Goodbye, {user_name}! Have a wonderful day! 👋")
        break
    elif "joke" in user_input:
        print("Bot: Why did the Python programmer go broke? Because he couldn't C#! 😄")
    else:
        print("Bot: Hmm, I'm not sure how to respond to that. Can you tell me more or ask something else?")
