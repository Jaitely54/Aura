#                                                      Radhe Radhe


#                                      A.U.R.A : Assistant for User Response and Automation

#  importing necessary libraries -------------->
import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser
import random
import requests
# import Speedtest
import math
import warnings
warnings.simplefilter('ignore')

#  Creating a function for the voice of the Assistant ------------>
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    id = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    engine.setProperty('voice',id)
    newVoiceRate = 150
    engine.setProperty('rate',newVoiceRate)
    engine.say(text=text)
    engine.runAndWait()




# Creating a function for the Assistant to listern us -------->
    
def takecmd():
    r = sr.Recognizer()
    with sr.Microphone() as src:
        print("Awaiting for command...")
        r.pause_threshold = 3
        r.energy_threshold = 300
        audio = r.listen(src,0,5)

    try:
        print("understanding...")
        query = r.recognize_google(audio,language="en-in")
        print(f"user: {query}\n")

    except Exception as e:
        print("aayien!! ?")
        return "None"
    
    return query

# creating Functions perform by the Assistant ----------> 


     
def greet():
    
    current_hour = int(datetime.datetime.now().hour)

    if current_hour < 12:
        greeting_message = "Good morning!"
    elif current_hour < 18:
        greeting_message = "Good afternoon!"
    else:
        greeting_message = "Good evening!"

    message = greeting_message +"Is there anything I can do for you?"
    speak(message)


def currenttime():
    currenttime = datetime.datetime.now()
    time1 = currenttime.strftime("%I %M:%p")
    print(f"the current timimg is: {time1}")
    speak(f"the current timimg is: {time1}")
    

def Currentdate():
    currenttime = datetime.datetime.now()
    date1  = currenttime.strftime("%A, %d/%m/%Y")
    print(f"the current Date is: {date1}")
    speak(f"the current Date is: {date1}")

def google_search(query):
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)



reboot_1 = ["reboot the system","reboot the laptop","reboot system","shutdown the laptop",
             "shutdown the system" , "shutdown system" ,"restart the laptop","restart the system", "restart system","shutdown the pc",
             "restart the pc", "reboot the pc"]

def reboot():
    for reboot_string in reboot_1:
        if reboot_string in query:
            print("do you want me to restart the system or shut it down ?")
            speak("do you want me to restart the system or shut it down ?")
            print("use cancel to aboort the task")
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
                    print("Aura: task aborted")
                    speak("task aborted")
                    break 

def get_weather(api_key, city):

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # You can change units to 'imperial' for Fahrenheit
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
            speak(f"its{temperature}°Celcius & {humidity}% Humidity")
        else:
            print(f"Error: {data['message']}")

    except Exception as e:
        print(f"An error occurred: {e}") 


def automate_os_commands(command):
    try:
        os.system(command)
        print(f"Aura: Executed the command: {command}")
        speak(f"Executed the command: {command}")
    except Exception as e:
        print(f"Aura: Error executing the command: {e}")
        speak("Sorry, there was an error executing the command.")

        
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
    user_input =query.lower()

    # Checking if any pattern is present in the user input
    if any(pattern in user_input for pattern in greetings["patterns"]):
        response = random.choice(greetings["responses"])
        print("Assistant:", response)
        speak(response)
    else:
        print("Assistant: I'm here to help. Feel free to ask anything!")
        speak(" I'm here to help. Feel free to ask anything!")

def generate_response():
    patterns = ["thank you", "thanks", "well done", "thank you so much", "thanks a lot", "nice"]
    responses = ["You're welcome!", "Happy to help!", "Glad I could assist.", "Anytime!", 
                 "You're welcome! Have a great day.", "No problem!"]

    # Taking user input (you can replace this with your speech recognition logic)
    user_input = query.lower()

    # Checking if any pattern is present in the user input
    if any(pattern in user_input for pattern in patterns):
        response = random.choice(responses)
        print("Assistant:", response)
        speak(response)
    else:
        print("Assistant: I'm here to help. Feel free to ask anything!")
        speak("I'm here to help. Feel free to ask anything!")
 





#  Executing the commands-------------->
    
while True:
    query = takecmd().lower()



        #  Starting the Assistant with a Wake up call --------->
    if "aura" in query:
        greet()

        while True:
            query = takecmd().lower()


            if any(keyword in query for keyword in reboot_1):

                reboot()

            elif "weather" in query:
                api_key = "ed7dbeaeb3f6b01d93a54e3e75a1830b"
                city = input("Please provide the city name: ")
        
                weather_result = get_weather(api_key, city)
                print("Aura:", weather_result)

            elif "google" in query or "search" in query or "browse" in query:

                google_search(query)


            elif "thank you" in query or "thanks" in query or "good job" in query or "well done" in query:
                generate_response()

            elif "time" in query:
                currenttime()

            elif "date" in query:
                Currentdate()

            elif "run command" in query or "execute command" in query:
                speak("Sure, please provide the command you want to execute.")
                command = takecmd().lower()
                automate_os_commands(command)

            # elif "calculate" in query or "calculator" in query:
            #     print("Aura:", calculator_result)
            #     speak(calculator_result)
            #     continue

            elif "hi" in query or "hello" in query or "hey" in query:
                welcome_response()


            # elif "internet speed" in query:
            #         wifi  = Speedtest.Speedtest()
            #         upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
            #         download_net = wifi.download()/1048576
            #         print("Wifi Upload Speed is", upload_net)
            #         print("Wifi download speed is ",download_net)
            #         speak(f"Wifi download speed is {download_net}")
            #         speak(f"Wifi Upload speed is {upload_net}")
                

            #  exiting the Assistant wiht the end call command ---------->
                
            elif "exit" in query or "kill" in query:

                print("Glad to work with you")
                speak("Glad to work with you")
                exit()
                
            

    elif "friday" in query:
        print("Aura: What The FUck!!")
        speak("What the FUck, did you forget me ? ")
        
    else:
        speak("Aura is set to sleep, wake her up")



