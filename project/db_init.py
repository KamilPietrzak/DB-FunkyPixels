from colorama import *
from dotenv import load_dotenv
from pathlib import *
import os
import psycopg2 as db

load_dotenv()

just_fix_windows_console()
init(autoreset=True)

print(Fore.BLUE + """
  /^ ^\\      
 / 0 0 \\     ███████ ██    ██ ███    ██ ██   ██ ██    ██     ██████  ██ ██   ██ ███████ ██      ███████ 
 V\ Y /V     ██      ██    ██ ████   ██ ██  ██   ██  ██      ██   ██ ██  ██ ██  ██      ██      ██      
  / - \\      █████   ██    ██ ██ ██  ██ █████     ████       ██████  ██   ███   █████   ██      ███████ 
 /    |      ██      ██    ██ ██  ██ ██ ██  ██     ██        ██      ██  ██ ██  ██      ██           ██ 
V__) ||      ██       ██████  ██   ████ ██   ██    ██        ██      ██ ██   ██ ███████ ███████ ███████
""")
print("\n" + Fore.BLUE + "=======================================================================================================")
print("\n" + Back.BLUE + Fore.BLACK + "Repozytory:" + Back.RESET + Fore.GREEN + " DB-FunkyPixels")
print("\n" + Fore.BLUE + "=======================================================================================================")
print("\n" + Back.MAGENTA + Fore.BLACK + "Email:" + Back.RESET + Fore.MAGENTA + " monetapietrzak@gmail.com")
print("\n" + Back.MAGENTA + Fore.BLACK + "Website:" + Back.RESET + Fore.MAGENTA + " www.monetapietrzak.com")
print("\n" + Fore.BLUE + "=======================================================================================================")

print(".env is exist?: " + str(Path('.env').exists()))

try:
    db.connect(host=os.getenv('HOST'), port=os.getenv('PORT'), user=os.getenv('USER'), password=os.getenv('PASSWORD'))
except db.OperationalError as error:
    if "password authentication failed" in error.args[0]:
        print("Password or user authentication failed.")
    elif "Unknown host" in error.args[0]:
        print("Unknown host.")
    elif "Connection refused" in error.args[0]:
        print("Bad port.")
    else:
        print(error)