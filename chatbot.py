import nltk
from nltk.chat.util import Chat, reflections

# Define patterns for the chatbot
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hey there!', 'Hi!']),
    (r'how are you?', ['I am fine, thank you!', 'I am doing well, thanks for asking.']),
    (r'what is your name?', ['You can call me Chatbot.', 'I am Chatbot.']),
    (r'quit', ['Bye! Take care.', 'Goodbye!']),
]

# Create a Chat object
chatbot = Chat(patterns, reflections)

# Start chatting
print("Hello! I am a chatbot. You can start chatting with me. Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    response = chatbot.respond(user_input)
    print("Bot:", response)
    if user_input.lower() == 'quit':
        break
