# Made by Kitten Team in Brazil :)

from ast import Store
from operator import rshift
import subprocess
import os

width = os.get_terminal_size().columns

print("================================".center(width))
print("| Howdy Folks! Welcome to LTB! |".center(width))
print("================================".center(width))
print("Now, what you wanna do?".center(width))
print("1- Let's use LTB!".center(width))
print("3- Downloader (BETA)".center(width))
print("4- Look our Github page!".center(width))
print("5- What's LTB?".center(width))
print("6- Let me out! (quit)".center(width))

slt = int(input(':'.center(width)))
print("\033[;5;31;31m Bright Green  \n")

if slt == 1:
    print("====================================================".center(width))
    print("|                 LTB Options list                 |".center(width))
    print("====================================================".center(width))

elif slt == 2:
    print("====================================================".center(width))
    print("|            Oh, so you have an suggestion?        |".center(width))
    print("====================================================".centerwidth)
    print("Nice to hear! Sadly, Due to lack of experience, we".center(width))
    print("can't add this now! But you can contact us in TG!".center(width))
    print("@krebox @akirawa1")
    print("")

elif slt == 3:
    print("====================================================")
    print("|           Not avaliable yet! We're Sorry!        |")
    print("====================================================")
    print("")

elif slt == 4:
    print("====================================================")
    print("|            Hmm... Where did you get this?        |")
    print("====================================================")
    print("| Anyways, there you go! |")
    print("| https://github.com/AkiraW5/LTB_Coding |")

elif slt == 6:
    quit