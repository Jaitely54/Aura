# Importing necessary libraries
import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser
import random
import requests

import warnings
warnings.simplefilter('ignore')

# Creating a function for the voice of the Assistant
def speak(text, voice="Zira"):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    
    # Set the voice based on the parameter
    if voice.lower() == "david":
        engine.setProperty('voice', voices[0].id)  # David's voice
    else:
        engine.setProperty('voice', voices[1].id)  # Zira's voice

    newVoiceRate = 150
    engine.setProperty('rate', newVoiceRate)
    engine.say(text=text)
    engine.runAndWait()

# Rest of your code...

# Example usage:
speak("Hello, how can I help you?", voice="David")
speak("Good morning! What can I do for you?", voice="Zira")
