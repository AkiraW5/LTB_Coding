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
import sys
import time
from time import sleep

colorama.init(autoreset=True)
os.system("pip install colorama")

width = os.get_terminal_size().columns

words = """
================================
| Howdy Folks! Welcome to LTB! |
================================
Now, what you wanna do?
1- Let's use LTB!
2- Want to suggest us something?
3- Downloader (BETA)
4- Look our Github page!
5- What's LTB?
6- Let me out! (quit)\n"""

C = Fore.BLUE + Back.BLACK
C1 = Fore.GREEN + Back.BLACK
version = platform.version()
release = platform.release()
machine = platform.machine()
GetUser = getpass.getuser()
UserInf = Back.BLACK + 'LINUX TOOLBOX' + Fore.BLUE + ' 0.1 ' + Fore.WHITE + ' | ' + Fore.BLUE + machine + Fore.WHITE + ' | ' + 'USER: ' + Fore.YELLOW + GetUser.upper(
) + Fore.WHITE + ' | '
UserInf2 = Back.BLACK + 'YOUR CURRENT SO: ' + Fore.GREEN + release + Fore.WHITE + ' | ' + 'VERSION: ' + Fore.GREEN + version + Fore.WHITE + ' | '

x = str(words)

opcao = 0


def Use_ltb(opcao):

    subprocess.run('clear')
    typewriter(
        "====================================================".center(width))
    typewriter(
        "|                 LTB Options list                 |".center(width))
    typewriter(
        "====================================================".center(width))

    print(Back.BLACK + '-' * width)
    print(Back.BLACK + Fore.RED + '0- ' + Fore.GREEN + 'Back to menu')
    print(Back.BLACK + '-' * width)

    opcao1 = input(Fore.YELLOW + Back.BLACK + 'Type option: ')

    while opcao1 != '0':

        if opcao1 == '0':
            menu(opcao1)

        elif opcao1 < '0':
            subprocess.run('clear')
            txt = 'ERROR: YOU NEED SELECT SOME OPTION'
            print(Back.BLACK + Fore.RED + '=' * width)
            print(Back.BLACK + Fore.RED + txt.center(width))
            print(Back.BLACK + Fore.RED + '=' * width)
            ctn = input(Fore.YELLOW + Back.BLACK +
                        'Type anything to continue: ')
            Use_ltb(opcao1)

        else:
            subprocess.run('clear')
            txt = 'ERROR: PLEASE TYPE A VALID OPTION'
            print(Back.BLACK + Fore.RED + '=' * width)
            print(Back.BLACK + Fore.RED + txt.center(width))
            print(Back.BLACK + Fore.RED + '=' * width)
            ctn = input(Fore.YELLOW + Back.BLACK +
                        'Type anything to continue: ')
            Use_ltb(opcao1)

        break


def typewriter(message):
    started = False
    for char in message:
        sys.stdout.write(Fore.BLUE + Back.BLACK + char)
        sys.stdout.flush()
        if char != " ":
            started = True
        if started:
            time.sleep(0.0001)


def menu(opcao):
    while opcao != '6':

        def character_info():

            subprocess.run('clear')
            print(Back.BLACK + Fore.WHITE + '=' * width)
            print(UserInf.ljust(width))
            print(UserInf2)
            print(Back.BLACK + Fore.WHITE + '=' * width)
            typewriter("================================".center(width))
            typewriter("| Howdy Folks! Welcome to LTB! |".center(width))
            typewriter("================================".center(width))
            typewriter("Now, what you wanna do?".center(width))
            typewriter("1- Let's use LTB!".center(width))
            typewriter("2- Want to suggest us something?".center(width))
            typewriter("3- Downloader (BETA)".center(width))
            typewriter("4- Look our Github page!".center(width))
            typewriter("5- What's LTB?".center(width))
            typewriter("6- Let me out! (quit)\n".center(width))
            print('')
            opcao = input(Fore.YELLOW + Back.BLACK + 'Type option: ')

        character_info()

        if opcao == '1':
            Use_ltb(opcao)

        elif opcao == '2':
            Suggest(opcao)

        elif opcao == '3':
            Downloader(opcao)

        elif opcao == '4':
            GitHub_Page(opcao)

        elif opcao == '5':
            print('5')
            break

        elif opcao == '6':
            quit
        print('dasdsa')
        elif opcao < '0':
            subprocess.run('clear')
            txt = 'ERROR: YOU NEED SELECT SOME OPTION'
            print(Back.BLACK + Fore.RED + '=' * width)
            print(Back.BLACK + Fore.RED + txt.center(width))
            print(Back.BLACK + Fore.RED + '=' * width)
            ctn = input(Fore.YELLOW + Back.BLACK +
                        'Type anything to continue: ')

        else:
            subprocess.run('clear')
            txt = 'ERROR: PLEASE TYPE A VALID OPTION'
            print(Back.BLACK + Fore.RED + '=' * width)
            print(Back.BLACK + Fore.RED + txt.center(width))
            print(Back.BLACK + Fore.RED + '=' * width)
            ctn = input(Fore.YELLOW + Back.BLACK +
                        'Type anything to continue: ')


menu(opcao)
