import speech_recognition as sr
from pathlib import Path
import wave
import contextlib

def recognize_from_microphone():
    """
    Captures audio from microphone and converts it to text.
    Returns the recognized text or error message.
    """
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait...")
        recognizer.adjust_for_ambient_noise(source, duration=2)
        print("Ready! Please speak...")
        
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=15)
            print("Processing speech...")
            
            # Using Google's speech recognition
            text = recognizer.recognize_google(audio)
            return text
            
        except sr.WaitTimeoutError:
            return "No speech detected within timeout period"
        except sr.UnknownValueError:
            return "Could not understand the audio"
        except sr.RequestError as e:
            return f"Could not request results; {e}"

def recognize_from_file(audio_file_path):
    """
    Converts speech from an audio file to text.
    Supports common audio formats (WAV, AIFF, AIFF-C, FLAC).
    
    Args:
        audio_file_path (str): Path to the audio file
    Returns:
        str: Recognized text or error message
    """
    recognizer = sr.Recognizer()
    
    try:
        with sr.AudioFile(audio_file_path) as source:
            audio = recognizer.record(source)
            
        # Using Google's speech recognition
        text = recognizer.recognize_google(audio)
        return text
        
    except FileNotFoundError:
        return "Audio file not found"
    except sr.UnknownValueError:
        return "Could not understand the audio"
    except sr.RequestError as e:
        return f"Could not request results; {e}"

def get_audio_duration(audio_file_path):
    """
    Gets the duration of an audio file in seconds.
    
    Args:
        audio_file_path (str): Path to the WAV file
    Returns:
        float: Duration in seconds
    """
    with contextlib.closing(wave.open(audio_file_path, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        return frames / float(rate)

