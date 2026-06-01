#by Sameer Rahil 

import string

def build_exact_responses():
    return {
        "hello": "Hi there! I am DecodeBot. How can I help you today?",
        "hi": "Hello! I am ready to chat with you.",
        "hey": "Hey! What would you like to ask me?",
        "good morning": "Good morning! I hope you have a productive day.",
        "good evening": "Good evening! How can I help you?",
        "how are you": "I am running smoothly. Thanks for asking.",
        "what is your name": "My name is DecodeBot, a simple rule based AI chatbot.",
        "who are you": "I am a rule based chatbot created for DecodeLabs AI Project 1.",
        "what can you do": "I can answer predefined questions, respond to greetings, explain simple AI concepts, and exit when you ask me to.",
        "help": "You can ask me about AI, chatbots, Python, DecodeLabs, or type exit to stop.",
        "what is ai": "Artificial Intelligence is the idea of making machines perform tasks that usually need human intelligence.",
        "what is artificial intelligence": "Artificial Intelligence means creating systems that can make decisions, solve problems, or respond intelligently.",
        "what is a chatbot": "A chatbot is a program that communicates with users through text or speech.",
        "what is a rule based chatbot": "A rule based chatbot follows predefined rules and gives responses based on known inputs.",
        "what is python": "Python is a beginner friendly programming language often used in AI, automation, and web development.",
        "what is decodelabs": "DecodeLabs is the organization assigning this internship project.",
        "tell me a joke": "Why did the programmer quit his job? Because he did not get arrays.",
        "joke": "Why do Python developers wear glasses? Because they cannot C.",
        "thank you": "You are welcome.",
        "thanks": "No problem. Happy to help.",
        "nice": "Glad you liked it.",
        "great": "Great! Keep going.",
        "internship": "This project is part of the DecodeLabs internship foundation phase.",
        "project": "Project 1 is about creating a rule based chatbot using control flow and logic."
    }


def build_keyword_rules():
    return {
        "ai": "AI is about building systems that can make decisions or respond intelligently.",
        "artificial intelligence": "Artificial Intelligence focuses on making machines behave intelligently.",
        "chatbot": "A chatbot is a program that talks to users using predefined or learned responses.",
        "python": "Python is a popular language for AI because it is simple, readable, and powerful.",
        "decodelabs": "DecodeLabs assigned this task to help interns understand basic AI logic.",
        "internship": "This internship project helps you move from learning code to building projects.",
        "rule": "Rule based systems use fixed logic to decide what response should be given.",
        "logic": "Logic is the decision making structure that controls how this chatbot responds.",
        "control flow": "Control flow decides which block of code runs based on conditions.",
        "dictionary": "A dictionary stores key value pairs and allows fast response lookup.",
        "fallback": "A fallback response is used when the chatbot does not understand the input."
    }


# cleans the user input
def clean_text(text):
    text = text.lower().strip()
    cleaned = ""

    for character in text:
        if character not in string.punctuation:
            cleaned += character

    words = cleaned.split()
    return " ".join(words)


#checks whether the user wants to exit
def is_exit_command(user_input):
    exit_commands = {"bye", "exit", "quit", "stop", "goodbye", "see you"}
    return user_input in exit_commands


#creates a response for unknown input
def fallback_response(user_input):
    if user_input == "":
        return "Please type something so I can respond."

    if "?" in user_input:
        return "I do not know the answer to that question yet, but I can learn it if my rules are updated."

    return "I do not understand that yet. Try asking about AI, chatbots, Python, or DecodeLabs."


#finds the best response
def get_response(user_input, exact_responses, keyword_rules):
    if user_input in exact_responses:
        return exact_responses[user_input]

    for keyword in keyword_rules:
        if keyword in user_input:
            return keyword_rules[keyword]

    return fallback_response(user_input)


def show_welcome_message():
    print()
    print("DecodeBot")
    print("Rule Based AI Chatbot")
    print()
    print("Type hello, help, what is ai, what is a chatbot, or exit.")
    print()


def main():
    exact_responses = build_exact_responses()
    keyword_rules = build_keyword_rules()

    show_welcome_message()

    while True:
        raw_input_text = input("You: ")
        user_input = clean_text(raw_input_text)

        if is_exit_command(user_input):
            print("Bot: Goodbye! Project 1 chatbot session ended.")
            break
        else:
            response = get_response(user_input, exact_responses, keyword_rules)
            print("Bot:", response)


if __name__ == "__main__":
    main()