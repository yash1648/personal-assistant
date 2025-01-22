import nltk


class app:
    task_patterns={
            "what's current time":["what is current time","what time is it","whats time","time"],
            "tell joke":["tell me a joke","tell a random joke","prepare a joke","tell a joke"]
        }
    def __init__(self):
        
        # Download required NLTK resources
        nltk.download('punkt')
        nltk.download('stopwords')
        nltk.download('wordnet')
        

    


    def run():
        print("Hello world")



