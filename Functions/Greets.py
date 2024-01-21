import pyttsx3 
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
id = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice',id)
newVoiceRate = 150
engine.setProperty('rate',newVoiceRate)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greet():
    current_hour = int(datetime.datetime.now().hour)

    if current_hour < 12:
        greeting_message = "Good morning!"
    elif current_hour < 18:
        greeting_message = "Good afternoon!"
    else:
        greeting_message = "Good evening!"


    engine.say(greeting_message)
    engine.runAndWait()
        
    speak("Is there anything I can do for you?")


greet()