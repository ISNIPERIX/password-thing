import time
import colorama
import os
import keyboard
from os import system, name 
from time import sleep
from colorama import Fore, Style, init
init()

def xauth():
    print("Successfully authenticated.")
    print("Please wait..")
    time.sleep(0)
    os.system('cls')
    rpassword = "passwordhere"
    apassword = "passwordhere"
    discpassword = "passwordhere"
    gitpassword = "passwordhere"
    ttpassword = "passwordhere"
    tpassword = "passwordhere"
    igpassword = "passwordhere"
    print("Press ALT to exit.")
    print(f"ROBLOX: {rpassword}")
    print(f"Discord: {discpassword}")
    print(f"Twitter: {tpassword}")
    print(f"Instagram: {igpassword}")
    print(f"Tiktok: {ttpassword}")
    print(f"Github: {gitpassword}")
    print(f"Amazon: {apassword}")
    while True:
        if keyboard.is_pressed(f'alt'):
            break

def auth():
    os.system('cls')
    print(f"{Fore.CYAN}{Style.BRIGHT}Welcome, {accounts.get(username)}.")
    print("Please wait..")
    time.sleep(1)
    os.system('cls')
    print("Please enter the second password, to verify it's you.")
    account2fa = {"root1" : "root1"}
    username2fa = input("Username: ")
    password2fa = input("Password: ")
    if (account2fa.get(username2fa) == password2fa):
        print("Logged in. Please wait..")
        xauth()
    else:
        print("Incorrect password.")


print(f"{Fore.RED}{Style.BRIGHT}Loading...")
time.sleep(1)
print(f"{Fore.GREEN}{Style.BRIGHT}Loading success.")
time.sleep(1)
os.system('cls')
time.sleep(0)
accounts = {"root" : "root"}
username = input("Username: ")
password = input("Password: ")
if (accounts.get(username) == password):
    print("Logged in. Please wait..")
    auth()
else:
    print("Incorrect password.")