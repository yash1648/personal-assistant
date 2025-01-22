from src import app 
from src.components.recognize import Recog
from src.components.taskHandler import joke
import src.components.tokenizer as tokenizer
if "__main__" == __name__ :
    assistant = Recog("Yash")
    assistant.say("Hello, how can I help you?")
    command = assistant.listen()
    output_text=tokenizer.preprocess_input(command)
    text=tokenizer.find_best_match(output_text)
    print(text)
    if text=="tell joke":
        assistant.say(joke())


    
    






