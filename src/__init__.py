import nltk
from .components.recognize import Recog
from .components.taskHandler import joke,currenttime
from .components import tokenizer

class Boa():
    """
    Main task to execute the code
    """
    task_patterns={
            "what's current time":["what is current time","what time is it","whats time","time"],
            "tell joke":["tell me a joke","tell a random joke","prepare a joke","tell a joke"],
            "greet":["hello","hello boa","greetings boa","hi","hii boa"],
            "good morning":["hello","hello boa good morning","greetings boa good morning","hi good morning","hii boa good morning"],
            "good afternoon":["hello","hello boa good afternoon","greetings boa good afternoon","hi good afternoon","hii boa good afternoon"],
            "good night":["hello","hello boa good night","greetings boa good night","hi good night","hii boa good night"],
            "who are you":["who are you?","what is your name ","whats your name","who are you"],
            "who am i ":["who am i","who i am ","who is your owner","who own you","who is your master"],

        }
    
    

    def run(self):
            
                assistant = Recog("Boa")
                assistant.say("Hello, how can I help you?")
                command = assistant.listen()
                output_text=tokenizer.preprocess_input("tell me a joke")
                text=tokenizer.find_best_match(output_text)
                print(text)
                if text=="tell joke":
                    assistant.say(joke())
                if text=="what's current time":
                       assistant.say("current time is : "+currenttime())
                       
                       
                     


