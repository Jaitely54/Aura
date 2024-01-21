#                                                           RADHE RADHE

# Importing necessary libraries
import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser
import random
import requests
import wikipedia

import warnings
warnings.simplefilter('ignore')

# Creating a function for the voice of the Assistant


def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    id = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    engine.setProperty('voice', id)
    newVoiceRate = 150
    engine.setProperty('rate', newVoiceRate)
    engine.say(text=text)
    engine.runAndWait()

# Creating a function for the Assistant to listen to us


def takecmd():
    r = sr.Recognizer()
    with sr.Microphone() as src:
        print("Aura: Awaiting for command...")
        r.pause_threshold = 2
        r.energy_threshold = 300
        audio = r.listen(src, 0, 4)

    try:
        print("Understanding...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User: {query}\n")
    except Exception as e:
        print("Aura: Aayien!! ?")
        return "None"
    return query

# Functions performed by the Assistant

# Greeting Function on wake up


def greet():
    current_hour = int(datetime.datetime.now().hour)
    if current_hour < 12:
        greeting_message = "Good morning!"
    elif current_hour < 16:
        greeting_message = "Good afternoon!"
    else:
        greeting_message = "Good evening!"

    message = f"{greeting_message} Is there anything I can do for you?"
    speak(message)

# Tells the current time


def currenttime():
    currenttime = datetime.datetime.now()
    time1 = currenttime.strftime("%I %M:%p")
    print(f"The current timing is: {time1}")
    speak(f"The current timing is: {time1}")

# Tells the current day/date


def Currentdate():
    currenttime = datetime.datetime.now()
    date1 = currenttime.strftime("%A, %d/%m/%Y")
    print(f"The current Date is: {date1}")
    speak(f"The current Date is: {date1}")

# Gives you the current weather update


def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']

            print(f"Weather in {city}: {weather_description}")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            speak(f"It's {temperature}°C with {humidity}% Humidity")
        else:
            print(f"Error: {data['message']}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Opens browser and searches the content for you


def google_search(query):
    speak("This is what I found for your search!")
    query = query.replace("google search", "").replace(
        "search", "").replace("aura", "").replace("google", "")
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)


# Controls the OS with voice
reboot_1 = ["reboot the system", "reboot the laptop", "reboot system", "shutdown the laptop",
            "shutdown the system", "shutdown system", "restart the laptop", "restart the system", "restart system",
            "shutdown the pc", "restart the pc", "reboot the pc"]

#  list of features
features_list = [
    "Wake-up Call",
    "Time and Date Information",
    "Weather Updates",
    "Web Search",
    "Boredom Buster",
    "System Control",
    "Interactive Greetings",
    "Thank You Responses",
    "Sleep Mode",
    "Location-Based Weather",
]

def featured_list():
    print("Available Features:")
    print(featured_list)
    speak(featured_list)


def reboot():
    for reboot_string in reboot_1:
        if reboot_string in query:
            print("Do you want me to restart the system or shut it down?")
            speak("Do you want me to restart the system or shut it down?")
            print("\n***Use 'cancel' to abort the task***")
            while True:
                user_input = takecmd().lower()

                if "restart" in user_input:
                    print("Restarting the system")
                    speak("Restarting the system")
                    os.system("shutdown /r /t 1")
                elif "shutdown" in user_input:
                    print("Shutting down the system")
                    speak("Shutting down the system")
                    os.system("shutdown /s /t 1")
                elif "cancel" in user_input:
                    print("Aura: Task aborted")
                    speak("Task aborted")
                    break

    #  seearch wiki ----------->


def wikipedia1(query):
    speak('Searching internet...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    print(results)
    speak(results)

    #  get bored ------------>


def get_me_suggestion(*args, **kwargs):
    url = 'http://www.boredapi.com/api/activity'
    response = requests.get(url)
    return response.json()['activity']


# Welcome function
def welcome_response():
    greetings = {
        "patterns": ["hello", "hi", "hey", "howdy", "greetings", "good morning",
                     "good afternoon", "good evening", "hi there", "hey there", "what's up", "hello there"],
        "responses": [
            "Hello! How can I assist you?", "Hi there!", "Hey! What can I do for you?",
            "Howdy! What brings you here?", "Greetings! How may I help you?",
            " How can I be of service?", " What do you need assistance with?",
            " How may I assist you?", "Hey there! How can I help?",
            "Hi! What's on your mind?", "Hello there! How can I assist you today?",
            "Hey! What's up?", "Hi there! Ready to help.", "Hello! What brings you here?",
            "Hi! How can I assist you today?", "Greetings! What can I do for you?",
            " Ready to assist.", " How may I help?",
            " Ready to assist.", "Hi there! What's on your mind?",
            "Hey there! Ready to help.", "Hello! Ready to assist."
            # Add more responses as needed
        ]
    }

    # Taking user input (you can replace this with your speech recognition logic)
    user_input = query.lower()

    # Checking if any pattern is present in the user input
    if any(pattern in user_input for pattern in greetings["patterns"]):
        response = random.choice(greetings["responses"])
        print("aura:", response)
        speak(response)
    else:
        print("aura: I'm here to help. Feel free to ask anything!")
        speak(" I'm here to help. Feel free to ask anything!")
# Thanks response


def thank_responses():
    patterns = ["thank you", "thanks", "well done",
                "thank you so much", "thanks a lot", "nice"]
    responses = [
        "You're welcome!",
        "Happy to help!",
        "Glad I could assist.",
        "Anytime!",
        "You're welcome! Have a great day.",
        "No problem!",
        "It was my pleasure!",
        "You got it!","No worries!","I'm here for you!","Don't mention it!","Not a problem!",
        "Anytime you need help, just ask!",
        "You're welcome! Let me know if there's anything else I can do for you.",
        "It's what I'm here for!",
        "Absolutely!",
        "I'm always here to assist you!",
        "You're welcome! If you have more questions, feel free to ask."]

    # Taking user input (you can replace this with your speech recognition logic)

    
    user_input = query.lower()  # Assuming query is the user's input

    # Checking if any pattern is present in the user input
    if any(pattern in user_input for pattern in patterns):
        response = random.choice(responses)
        print("Assistant:", response)
        speak(response)
    else:
        print("Assistant: I'm here to help. Feel free to ask anything!")
        speak(" I'm here to help. Feel free to ask anything!")


# Instructions before using
print("\nHey there, I am AURA, an AI-powered Desktop Assistant")
print("\nAURA is Sleeping, Wake her up")
print("\n***Clear Instruction for Aura***")

print("Certainly! To exit the program, you can use the command 'Exit'.")
print("Certainly! To make Aura go into sleep mode, you can use the command 'Sleep'.")
print("\n")

# Executing the commands
while True:
    query = takecmd().lower()

    # Starting the Assistant with a Wake-up call
    if "wake up" in query or " uth ja" in query or "good morning aura" in query or "aura" in query or "good evening aura" in query:

        greet()

        while True:
            query = takecmd().lower()

            if "time" in query:
                currenttime()

            elif "go to sleep" in query or "sleep mode" in query:

                speak("Going to sleep mode. Let me know when you need assistance.")
                break

            elif "weather" in query:

                api_key = "ed7dbeaeb3f6b01d93a54e3e75a1830b"
                print(
                    "i can't detect your current location, can you be specific which city you are in")
                speak(
                    "i can't detect your current location, can you be specific which city you are in")
                city = takecmd().lower()
                weather_result = get_weather(api_key, city)
                print("Aura:", weather_result)

            elif "features" in query or "available features" in query:
                featured_list()

            elif "date" in query:
                Currentdate()

            elif "i am bored" in query or "fun activity" in query:
                suggestion = get_me_suggestion()
                print("Aura:", suggestion)
                speak(suggestion)

            elif any(keyword in query for keyword in reboot_1):
                reboot()

            # elif "wikipedia" in query or "who is" in query:
            #     wikipedia1()

            elif "google" in query or "search" in query or "browse" in query:
                google_search(query)

            elif "thank you" in query or "thanks" in query or "good job" in query or "well done" in query:
                thank_responses()

            elif "hi" in query or "hello" in query or "hey" in query:
                welcome_response()

            # Exiting the Assistant with the end call command
            elif "exit" in query or "turn off" in query:
                print("Glad to work with you")
                speak("Glad to work with you")
                exit()

            # else:
            #     speak("i am still under development, i can't assist with that request right now")

    # else:
    #     speak("Aura is set to sleep, wake her up")
