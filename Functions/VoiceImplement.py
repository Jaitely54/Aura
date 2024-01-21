import pyttsx3
import speech_recognition as sr
import warnings
import datetime
warnings.simplefilter('ignore')

#  creating a function for the voice of the AI --------------->
engine = pyttsx3.init()
def speak(text):
    engine.setProperty('voice', r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
    engine.say(text=text)
    engine.runAndWait()

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    id = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    engine.setProperty('voice',id)
    newVoiceRate = 150
    engine.setProperty('rate',newVoiceRate)

    engine.say(text=text)
    engine.runAndWait()

    



#  creating a function to let the AURA listern us ----------------->

def takecmd():
    r = sr.Recognizer()
    with sr.Microphone() as src:
        print("Awaiting your command...")

        r.pause_threshold =2
        r.energy_threshold = 200
        audio = r.listen(src,0,4)

    try:
        print("understanding...")
        query = r.recognize_google(audio,language="en-in")
        print(f"user: {query}\n")

    except Exception as e:
        print("aayien!! ?")
        return "None"
    
    return query
        

   

 