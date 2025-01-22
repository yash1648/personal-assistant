import pyttsx3
import speech_recognition as sr

class Recog():
    def __init__(self, name=None):
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        
        
        print(voices[1].id)
        self.engine.setProperty('voice', voices[1].id)
        self.engine.setProperty('rate', 200)  # Default rate is around 200-250; lower for slower speed
        
        # Set volume (0.0 to 1.0)
        self.engine.setProperty('volume', 0.9)
        self.r = sr.Recognizer()
        self.m = sr.Microphone()
        self.__name = name if name is not None else ""
        
        print("Listening...")
        with self.m as source:
            self.r.adjust_for_ambient_noise(source)
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if self.__name:
            sentence = f"Hello, my name is {self.__name}"
            self.engine.say(sentence)
            self.engine.runAndWait()
        self.__name = value

    def say(self, sentence):
        """Speak the given sentence."""
        self.engine.say(sentence)
        self.engine.runAndWait()

    def listen(self):
        """Listen for user speech until complete."""
        print("Say something...")
        try:
            with self.m as source:
                self.r.adjust_for_ambient_noise(source, duration=1)
                print("Listening for your complete input...")
                audio = self.r.listen(source, timeout=None, phrase_time_limit=5)
            print("Processing...")
            phrase = self.r.recognize_google(audio, show_all=False, language="en-us")
            sentence = f"Got it, you said: {phrase}"
            self.say(sentence)
            print("You said:", phrase)
            return phrase
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            self.say("Sorry, I didn't catch that.")
        except sr.RequestError as e:
            print("Speech recognition service error:", e)
            self.say("Speech recognition service is not available.")

    
