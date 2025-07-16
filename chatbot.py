from langchain_community.llms import Ollama

lim= Ollama(model="llama3")

# chatbot.py (Offline mock version)

def get_bot_response(user_input):
    # Simple mock logic
    if "hello" in user_input.lower():
        return "Hi there! How can I help you today?"
    elif "bye" in user_input.lower():
        return "Goodbye! Have a great day!"
    else:
        return "This is a mock reply. Replace me with AI later!"