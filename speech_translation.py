import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os
from playsound import playsound
import threading

# Error messages to be returned in case of failure
ERROR_TEXT = "Error: Could not understand the audio."
SERVICE_ERROR = "Error: Speech recognition service failed."

# Function to record audio with an optional duration
def record_audio(duration=None):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Recording...")
        try:
            audio = recognizer.listen(source, timeout=duration)
            print("Recording complete.")
        except sr.WaitTimeoutError:
            print("Recording timeout. Please try again.")
            return None
    return audio

# Function to convert recorded audio into text
def speech_to_text(audio):
    recognizer = sr.Recognizer()
    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print(ERROR_TEXT)
        return ERROR_TEXT
    except sr.RequestError:
        print(SERVICE_ERROR)
        return SERVICE_ERROR

# Function to translate text into the target language
def translate_text(text, target_language='es'):
    translator = Translator()
    try:
        translated_text = translator.translate(text, dest=target_language).text
        print(f"Translated Text ({target_language}): " + translated_text)
        return translated_text
    except Exception as e:
        print(f"Translation error: {str(e)}")
        return f"Error in translating text to {target_language}"

# Function to convert text into speech and play it
def text_to_speech(text, language_code='es'):
    try:
        tts = gTTS(text=text, lang=language_code)
        tts.save("output.mp3")
        
        # Play the audio asynchronously using threading
        thread = threading.Thread(target=play_audio, args=("output.mp3",))
        thread.start()
    except Exception as e:
        print(f"Text-to-Speech error: {str(e)}")

# Helper function to play the audio
def play_audio(filename):
    try:
        playsound(filename)  # Platform-independent audio playback
    except Exception as e:
        print(f"Error playing audio: {str(e)}")

# Function to combine translation and speech generation
def translate_and_generate_speech(text, target_language='es'):
    translated_text = translate_text(text, target_language)
    if not translated_text.startswith("Error"):
        text_to_speech(translated_text, target_language)
    return translated_text

if __name__ == "__main__":
    # Example usage
    audio = record_audio()
    if audio:
        english_text = speech_to_text(audio)
        if not english_text.startswith("Error"):
            translate_and_generate_speech(english_text, 'fr')  # Example: Translate to French
