import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import os
import pyaudio

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Initialize the recognizer
recognizer = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(command):
    if "hello" in command:
        speak("Hello! How can I help you?")
    elif "What is weather today?" in command:
        speak("Yes, How can i help you out in this? Thank you for asking!")
    elif "what's your name" in command:
        speak("I'm a voice assistant. You can call me Assistant.")
    elif "goodbye" in command:
        speak("Goodbye! Have a nice day.")
        exit()
    else:
        speak("I'm sorry, I didn't get that.")

def main():
    speak("Hello! I'm your voice assistant. How can I assist you today?")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=10)

            command = recognizer.recognize_google(audio).lower()
            print("You said:", command)
            
            process_command(command)
            
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
        except sr.RequestError:
            print("Sorry, I'm having trouble with my speech recognition. Please try again later.")

if __name__ == "__main__":
    main()
