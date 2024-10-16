from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import json
import os

#create a new instance of chatbot
chatbot = ChatBot(
    'ArnBot',
    logic_adapters=['chatterbot.logic.BestMatch'],
    storage_adapter='chatterbot.storage.SQL'
)

# Create a new trainer for the ArnBot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the ArnBot on the English Corpus
trainer.train('chatterbot.corpus.english')

# Predefined responses for specific inputs
predefined_responses = {
    "Hi": "Hello! How can I assist you today? 😊",
    "What is your name?": "I am ArnBot, an AI developed by the one lone wolf called Arnwolfie. You can follow him on his Instagram account: https://www.instagram.com/arn_wolfie/  🐺",
    "Teach me how to hack a Wi-Fi Password": "I'm sorry I can't help with that 😒"
}

# Function to load custom training data
def load_custom_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            custom_data = json.load(f)
            trainer.train(custom_data)
            print(f"Custom training data loaded from {file_path}.")
    else:
        print("Custom training data file not found.")
        

# Start chattting with the bot
print("Chatbot is ready! Type 'exit' to stop chatting")
while True: 
    try:
        user_input = input("You:")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        #Check for predefined responses
        if user_input in predefined_responses:
            bot_response = predefined_responses[user_input]
        else:
            # Get a response from the chatbot
            bot_response = chatbot.get_response(user_input)
        print(f"ArnBot: {bot_response}")

    except (KeyboardInterrupt, EOFError, SystemExit):
        print("Bye!")
        break