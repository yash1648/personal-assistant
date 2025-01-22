import nltk
from .components.recognize import Recog
from .components.taskHandler import joke
from .components import tokenizer
import nltkdownloads as nl
class Boa():
    task_patterns={
            "what's current time":["what is current time","what time is it","whats time","time"],
            "tell joke":["tell me a joke","tell a random joke","prepare a joke","tell a joke"]
        }
    
    

    def run(self):
            try:
                assistant = Recog("Yash")
                assistant.say("Hello, how can I help you?")
                command = assistant.listen()
                output_text=tokenizer.preprocess_input(command)
                text=tokenizer.find_best_match(output_text)
                print(text)
                if text=="tell joke":
                    assistant.say(joke())
            except LookupError:
                     nl.install_nltk_resources()
                     print("Nltk downloaded successfull try relaunching the code...")
                     


