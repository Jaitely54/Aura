#                                                             RADHE RADHE
#?                                             A.U.R.A.(Assistant for User Response and Automation)



#-----------------------------------------------------------
print("\nHey there, I am AURA, an AI-powered Desktop Assistant")
print("\nAURA is Sleeping, Wake her up")
print("\n***Clear Instruction for Aura***")

print("Certainly! To start talking, use the wake up call 'Aura'. ")
print("Certainly! To exit the program, you can use the command 'Exit'.")
print("Certainly! To make Aura go into sleep mode, you can use the command 'Sleep'.")

print("\n")
#-----------------------------------------------------------

#!  getting the infomations of Available voices 
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')



    # Print details of all available voices
    # for voice in voices:
    #     print("----------------------------")
    #     print(f"Voice ID: {voice.id}")
    #     print(f"Voice Name: {voice.name}")
    #     print("----------------------------")
#* Voice ID: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0

    voice  =  engine.getProperty("voices")
    id = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    engine.setProperty('voice',id)
    newVoiceRate = 150      # Will Speak with 150 wpm
    engine.setProperty("rate",newVoiceRate)
    engine.say(text=text)
    engine.runAndWait()

#!Text-To-Speech
def takecmd():   
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Aura:Awaiting for command...")
        r.pause_threshold = 2   # pause_threshold: Silence duration to end speech (seconds).
        r.energy_threshold = 300       #energy_threshold: Noise level to consider as speech.
        audio = r.listen(source,0,4)
    try:
        print("Understanding...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User: {query}\n")
    except Exception as e:
        print("Aura: Aayien!! ?")
        return "None"
    return query

#-----------------------------------------------------------
#!  Functions of Aura:
#-----------------------------------------------------------

#! Geeting According to time.
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
#-----------------------------------------------------------
    
#! updating about Date & Time
def currenttime():      
    currenttime = datetime.datetime.now()
    time1 = currenttime.strftime("%I %M:%p")
    print(f"The current timing is: {time1}")
    speak(f"The current timing is: {time1}")

def Currentdate():
    currenttime = datetime.datetime.now()
    date1 = currenttime.strftime("%A, %D/%m/%Y")
    print(f"The current Date is: {date1}")
    speak(f"The current Date is: {date1}")
#-----------------------------------------------------------
#! Weather Updates
def get_city_from_ipinfo(api_token):    #Fetch the device Location
    try:
        response = requests.get(f'https://ipinfo.io?token={api_token}')
        data = response.json()
        return data['city']
    except Exception as e:
        print(f"Error obtaining city from IP: {e}")
        return None
    
def get_weather(api_key, city):     #Provides the Weather info of the location
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if response.status_code == 200:
            weather_description = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]

            weather_info = (f"Weather in {city}: {weather_description}\n"
                            f"Temperature: {temperature}°C\n"
                            f"Humidity: {humidity}%")
            return weather_info
        else:
            return f"Error fetching weather: {data['message']}"
    except Exception as e:
        return f"An error occurred: {e}"
#-----------------------------------------------------------
#! System Control (BASIC)
reboot_1 = [
    "reboot the system",
    "reboot the laptop",
    "reboot system",
    "shutdown the laptop",
    "shutdown the system",
    "shutdown system",
    "restart the laptop",
    "restart the system",
    "restart system",
    "shutdown the pc",
    "restart the pc",
    "reboot the pc",
]    
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
#-----------------------------------------------------------
                
    

#-----------------------------------------------------------
#! Executing Functions    
#-----------------------------------------------------------
while True:
    query = takecmd().lower()
    if ("wake up" in query or "aura" in query):
        greet()
        while True:
            query = takecmd().lower()

            #! Sleep mode
            if "go to sleep" in query:
                speak("Going to sleep mode, Let me know when you need assistance")
                break

            #! current time
            elif "time" in query:
                currenttime()

            #! weather update
            elif "weather update" in query:
                ipinfo_api_token = 'c9af1030a48637'  # Replace with your ipinfo.io API token
                openweathermap_api_key = 'ed7dbeaeb3f6b01d93a54e3e75a1830b'  # Replace with your OpenWeatherMap API key
    
                city = get_city_from_ipinfo(ipinfo_api_token)
                if city:
                    print(f"Detected city: {city}")
                    weather_info = get_weather(openweathermap_api_key, city)
                    print(weather_info)
                    speak(weather_info)
                else:
                    print("Could not detect city based on IP address.")

            #! current date
            elif "date" in query:
                Currentdate()

               

            #! system control
            elif any(keyword in query for keyword in reboot_1):
                reboot()  

            #! Exiting the program
            elif "exit" in query or "turn off" in query:
                print("Glad to work with you")
                speak("Glad to work with you")
                exit()
    else:
        print("Wake up Call: Say 'Aura' to wake her up" )
        speak("aura is sleeping, Wake her up")
    



