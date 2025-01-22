import pyttsx3
import speech_recognition as sr
import edge_tts
import asyncio
import os
from datetime import datetime
import random
from playsound import playsound
import glob 

class voice:
    """
    To create the natural voice 
    """
    NATURAL_VOICE_PRESETS = {
        "natural_confident": {
            "voice": "en-US-JennyMultilingualNeural",
            "rate": "+2%",
            "volume": "+20%",
            "pitch": "+1Hz",      # Corrected: Whole number
            "style": "friendly"
        },
        "natural_gentle": {
            "voice": "en-US-AriaNeural",
            "rate": "-3%",
            "volume": "+15%",
            "pitch": "+1Hz",      # Corrected: No fractional values
            "style": "calm"
        },
        "natural_professional": {
            "voice": "en-GB-SoniaNeural",
            "rate": "+0%",
            "volume": "+25%",
            "pitch": "0Hz",       # Neutral pitch
            "style": "professional"
        },
        "natural_warm": {
            "voice": "en-AU-NatashaNeural",
            "rate": "-1%",
            "volume": "+18%",
            "pitch": "+1Hz",      # Corrected
            "style": "friendly"
        },
        "natural_soft": {
            "voice": "ja-JP-NanamiNeural",
            "rate": "-2%",
            "volume": "+12%",
            "pitch": "+1Hz",      # Corrected
            "style": "gentle"
        },
        "one_for_all":{
            "voice": "ja-JP-NanamiNeural",
        "rate": "-2%",      # Slower rate to reflect hesitation
        "volume": "+5%",     # Slightly lower volume for subtlety
        "pitch": "-2Hz",     # Lower pitch to make it sound softer
        "style": "shy"       # Apply a shy speaking style
    }
                        
        
    }


    # Natural speech patterns for text preprocessing
    NATURAL_PATTERNS = {
        "pauses": [
            ", ",        # Short pause
            ". ",        # Normal pause
            "... ",      # Thoughtful pause
            "? ",        # Question pause
            "! "         # Emphatic pause
        ],
        "fillers": [
            "um",
            "uh",
            "hmm",
            "well",
            "you see"
        ]
    }

    def add_natural_pauses(self,text):
        """
        Add natural pauses and breathing points to the text
        """
        sentences = text.split('. ')
        enhanced_text = []
        
        for sentence in sentences:
            # Add occasional thoughtful pauses
            if random.random() < 0.2:
                sentence = sentence.replace(',', '... ')
            
            # Add slight pauses for emphasis
            if random.random() < 0.15:
                words = sentence.split()
                if len(words) > 4:
                    insert_pos = random.randint(2, len(words)-2)
                    words.insert(insert_pos, ',')
                    sentence = ' '.join(words)
                    
            enhanced_text.append(sentence)
        
        return '. '.join(enhanced_text)

    async def generate_natural_voice(self,text, output_file, preset_name=None, **kwargs):
        """
        Generate voice with natural speaking patterns
        """
        try:
            # Get preset parameters
            if preset_name and preset_name in self.NATURAL_VOICE_PRESETS:
                params = self.NATURAL_VOICE_PRESETS[preset_name].copy()
            else:
                params = kwargs
            
            # Add natural speech patterns
            enhanced_text = self.add_natural_pauses(text)
            
            # Create communicate instance with natural parameters
            communicate = edge_tts.Communicate(
                enhanced_text,
                params.get("voice", "en-US-JennyMultilingualNeural"),
                rate=params.get("rate", "+0%"),      # Default to natural pace
                volume=params.get("volume", "+20%"),  # Moderate default volume
                pitch=params.get("pitch", "+0Hz")     # Natural pitch
            )
            
            await communicate.save(output_file)
            return True
        except Exception as e:
            print(f"Error generating voice: {e}")
            return False



    def play_audio(self,file_path):
        """
        Playing the .mp3 file
        """
        try:
            playsound(file_path)
        except Exception as e:
            print(f"Error playing audio: {e}")


    async def main(self,text):
        """
        Main function to TTS
        """
        output_dir = "generated_audio"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        
        
        preset_name = "one_for_all"  
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = os.path.join(output_dir, f"natural_voice_{preset_name}_{timestamp}.mp3")
        print(output_file)
        print(f"Generating natural voice with {preset_name} preset...")
        success = await self.generate_natural_voice(text, output_file, preset_name=preset_name)
        
        if success:
            print(f"Playing {preset_name} preset...")
            self.play_audio(output_file)
            self.delete_files_from_folder(output_dir)

    def delete_files_from_folder(self,folder_path):
        """
        Deleting the temp mp3 file after execution
        """
        try:
            # Check if the folder exists
            if not os.path.exists(folder_path):
                print(f"Error: The folder {folder_path} does not exist.")
                return
            
            # Get all files in the folder and delete them
            files = glob.glob(os.path.join(folder_path, "*"))
            for file in files:
                os.remove(file)
                print(f"Deleted: {file}")
            
        except Exception as e:
            print(f"An error occurred: {e}")






class Recog():
    """
    speech recognition class
    """
    def __init__(self, name=None):
        """
        Initializing the voice and Recognizer 
        """
        self.engine=voice()
        self.r = sr.Recognizer()
        self.m = sr.Microphone()
        self.__name = name if name is not None else ""
        
        print("Listening...")
        with self.m as source:
            self.r.adjust_for_ambient_noise(source)
    
    @property
    def name(self):
        """
        Returning the name of the assistant
        """
        return self.__name

    @name.setter
    def name(self, value):
        """Set the name of the assistant"""
        if self.__name:
            sentence = f"Hello, my name is {self.__name}"
            self.engine.say(sentence)
            self.engine.runAndWait()
        self.__name = value

    def say(self,text):
        """Executing the TTS"""
        asyncio.run(self.engine.main(text))

    def listen(self):
        """Listen for user speech until complete."""
        print("Say something...")
        try:
            with self.m as source:
                self.r.adjust_for_ambient_noise(source, duration=1)
                print("Listening for your complete input...")
                audio = self.r.listen(source, timeout=None, phrase_time_limit=5)
            print("Processing...")
            phrase = self.r.recognize_google(audio, show_all=False, language="en_US")
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

    
