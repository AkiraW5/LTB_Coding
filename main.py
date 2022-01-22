# Made by Kitten Team in Brazil :)
import subprocess
from ast import Store
from operator import rshift
import os
import colorama
from colorama import Fore, Back, Style
import platform
import getpass

colorama.init(autoreset=True)
os.system("pip install colorama")
'''
Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL
'''

C = Fore.BLUE + Back.BLACK
C1 = Fore.GREEN + Back.BLACK

width = os.get_terminal_size().columns

texto = 'test'

version = platform.version()
release = platform.release()
machine = platform.machine()
username = getpass.getuser()
abacate = "teste"

print(
    C +
    f'{"=" * width}\n{release:<20}{machine:^20}{username:>20}\n{"=" * width}')

print(C + "================================".center(width))
print(C + "| Howdy Folks! Welcome to LTB! |".center(width))
print(C + "================================".center(width))
print(C + "Now, what you wanna do?".center(width))
print(C + "1- Let's use LTB!".center(width))
print(C + "2- Want to suggest us something?".center(width))
print(C + "3- Downloader (BETA)".center(width))
print(C + "4- Look our Github page!".center(width))
print(C + "5- What's LTB?".center(width))
print(C + "6- Let me out! (quit)".center(width))

slt = int(input(Fore.YELLOW + Back.BLACK + 'Type Option: '))

if slt == 1:
    subprocess.run('clear')
    print(C1 +
          "====================================================".center(width))
    print(C1 +
          "|                 LTB Options list                 |".center(width))
    print(C1 +
          "====================================================".center(width))

    print(C1 +
          "- - - - - - - - - - - - - - - - - - - - - - - - - - - -".center(
              width))
    print(C1 + "|[0] Back To Menu|".center(width))
    print(C1 +
          "- - - - - - - - - - - - - - - - - - - - - - - - - - - -".center(
              width))

    slt = int(input(Fore.YELLOW + Back.BLACK + 'Type Option: '))

elif slt == 2:
    subprocess.run('clear')
    print(C1 +
          "====================================================".center(width))
    print(C1 +
          "|            Oh, so you have an suggestion?        |".center(width))
    print(C1 +
          "====================================================".center(width))
    print(C1 +
          "Nice to hear! Sadly, Due to lack of experience, we".center(width))
    print(C1 +
          "can't add this now! But you can contact us in TG!".center(width))
    print(C1 + "@krebox @akirawa1".center(width))
    print("")

elif slt == 3:
    subprocess.run('clear')
    print(C1 +
          "====================================================".center(width))
    print(C1 +
          "|           Not avaliable yet! We're Sorry!        |".center(width))
    print(C1 +
          "====================================================".center(width))
    print("")

elif slt == 4:
    subprocess.run('clear')
    print(C1 +
          "====================================================".center(width))
    print(C1 +
          "|            Hmm... Where did you get this?        |".center(width))
    print(C1 +
          "====================================================".center(width))
    print(C1 + "| Anyways, there you go! |".center(width))
    print(C1 + "| https://github.com/AkiraW5/LTB_Coding |".center(width))

elif slt == 6:
    quit
