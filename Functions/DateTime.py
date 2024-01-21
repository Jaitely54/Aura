import datetime

def timemodule():
    currenttime = datetime.datetime.now()

    time1 = currenttime.strftime("%I:%M:%p")
    date1  = currenttime.strftime("%A, %d-%m-%Y")

    print(f"the current timimg is: {time1}\nits {date1}")

timemodule()

 

