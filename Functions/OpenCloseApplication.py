import os
import speech_recognition as sr
import pyttsx3


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def take_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Could you please repeat?")
        return ""
    except sr.RequestError as e:
        print(
            f"Error fetching results from Google Speech Recognition service; {e}")
        return ""


def open_application(application_name):
    try:
        os.system(f"start {application_name}")
        speak(f"Opening {application_name}")
    except Exception as e:
        print(f"Error opening application: {e}")
        speak("Sorry, I couldn't open the application.")


def close_application(application_name):
    try:
        os.system(f"taskkill /f /im {application_name}.exe")
        speak(f"Closing {application_name}")
    except Exception as e:
        print(f"Error closing application: {e}")
        speak("Sorry, I couldn't close the application.")


speak("Hello! I'm Aura. How can I assist you today?")

while True:
    command = take_command().lower()

    if "open" in command:
        # Extract the application name from the command
        application_name = command.replace("open", "").strip()
        open_application(application_name)

    elif "close" in command:
        # Extract the application name from the command
        application_name = command.replace("close", "").strip()
        close_application(application_name)

    elif "exit" in command or "quit" in command:
        speak("Goodbye! Have a great day.")
        break


