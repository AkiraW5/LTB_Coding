# Made by Kitten Team in Brazil :)
import subprocess
from ast import Store
from operator import rshift
import os
import colorama
from colorama import Fore, Back, Style
import platform
import getpass
import socket
import csv

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

version = platform.version()
release = platform.release()
machine = platform.machine()
GetUser = getpass.getuser()
UserInf = Back.BLACK + 'LINUX TOOLBOX' + Fore.BLUE + ' 0.1 ' + Fore.WHITE + ' | ' + Fore.BLUE + machine + Fore.WHITE + ' | ' + 'USER: ' + Fore.YELLOW + GetUser.upper(
) + Fore.WHITE + ' | '
UserInf2 = Back.BLACK + 'YOUR CURRENT SO: ' + Fore.GREEN + release + Fore.WHITE + ' | ' + 'VERSION: ' + Fore.GREEN + version + Fore.WHITE + ' | '

opcao = 0
while opcao != 6:
    print(Back.BLACK + Fore.WHITE + '=' * width)
    print(UserInf.ljust(width))
    print(UserInf2)
    print(Back.BLACK + Fore.WHITE + '=' * width)
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
    opcao = int(input(Fore.YELLOW + Back.BLACK + 'Type your option: '))

    if opcao == 1:
        subprocess.run('clear')
        print(C1 +
              "====================================================".center(
                  width))
        print(C1 +
              "|                 LTB Options list                 |".center(
                  width))
        print(C1 +
              "====================================================".center(
                  width))
        break

    elif opcao == 2:
        subprocess.run('clear')
        print(C1 +
              "====================================================".center(
                  width))
        print(C1 +
              "|            Oh, so you have an suggestion?        |".center(
                  width))
        print(C1 +
              "====================================================".center(
                  width))
        print(
            C1 +
            "Nice to hear! Sadly, Due to lack of experience, we".center(width))
        print(
            C1 +
            "can't add this now! But you can contact us in TG!".center(width))
        print(C1 + "@krebox @akirawa1".center(width))

        break

    elif opcao == 3:
        subprocess.run('clear')
        print(C1 +
              "====================================================".center(
                  width))
        print(C1 +
              "|           Not avaliable yet! We're Sorry!        |".center(
                  width))
        print(C1 +
              "====================================================".center(
                  width))
        print("")

        break

    elif opcao == 4:
        subprocess.run('clear')
        print(C1 +
              "====================================================".center(
                  width))
        print(C1 +
              "|            Hmm... Where did you get this?        |".center(
                  width))
        print(C1 +
              "====================================================".center(
                  width))
        print(C1 + "| Anyways, there you go! |".center(width))
        print(C1 + "| https://github.com/AkiraW5/LTB_Coding |".center(width))

        break

    elif opcao == 5:
        print('5')

    elif opcao == 6:
        quit

    else:
        subprocess.run('clear')
        txt = 'ERROR: PLEASE TYPE A VALID OPTION'
        print(Back.BLACK + Fore.RED + '=' * width)
        print(Back.BLACK + Fore.RED + txt.center(width))
        print(Back.BLACK + Fore.RED + '=' * width)
        ctn = input(Fore.YELLOW + Back.BLACK + 'Type anything to continue: ')

print('acabou')