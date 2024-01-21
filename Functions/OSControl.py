import os

# reboot_1 = ["reboot the system","reboot the laptop","reboot system","shutdown the laptop",
#              "shutdown the system" , "shutdown system" ,"restart the laptop","restart the system", "restart system","shutdown the pc",
#              "restart the pc", "reboot the pc"]

# promt = "reboot the system"


# for promt in reboot_1:

#     print("\n")
#     print('do you wish to reboot the pc or you wish to shut it down:\n')
#     n = input("Press 1 for reboot, Press 2 for shutdown, press any other key for cancelling the process:")
#     print("\n")
#     if n == "1":
#         print("Restarting the pc\n")
#         os.system("shutdown /r /t 1")

#     elif n == "2":
#         print("shutting down the pc")
#         os.system("shutdown /s /t 1")
#     else:
#         print("no rebooting/Shutdown will perform \n")
#         break

# print("Function will be working properly \n")
# os.system('---')


# calculator as calc
# calender as start outlook cal
# chrome as start chrome.exe
# edge as start msedge.exe
# paint as mspaint
# file explorer as explorer.exe
# powerpoint as start POWERPNT.EXE
# excel as start EXCEL.EXE
# word as start WINWORD.EXE

application_commands = {
    "calculator": "start calc.exe",
    "calender": "start outlook cal",
    "chrome": "start chrome.exe",
    "edge": "start msedge.exe",
    "paint": "mspaint",
    "file explorer": "explorer.exe",
    "powerpoint": "start POWERPNT.EXE",
    "excel": "start EXCEL.EXE",
    "word": "start WINWORD.EXE"
}


user_command = input("enter the application you want to start:")

if user_command in application_commands:
    command_to_execute = application_commands[user_command]
    os.system(command_to_execute)
else:
    print("Command not recognized.")


# import subprocess
# import re


# def get_installed_applications():
#     try:
#         # Get the list of installed programs using WMIC command
#         result = subprocess.check_output(['wmic', 'product', 'get', 'name'])
#         # Decode bytes to string and split by newline
#         programs = result.decode('utf-8').split('\n')
#         # Filter out empty lines and remove 'Name' header
#         programs = [program.strip() for program in programs if program.strip(
#         ) and program.strip() != 'Name']
#         # Create a dictionary with program names
#         app_dict = {f"app_{index + 1}": program for index,
#                     program in enumerate(programs)}
#         return app_dict
#     except Exception as e:
#         return f"Error: {e}"


# # Call the function to get the installed applications dictionary
# installed_applications = get_installed_applications()

# # Print the result
# if isinstance(installed_applications, dict):
#     for key, value in installed_applications.items():
#         print(f"{key}: {value}")
# else:
#     print(installed_applications)
