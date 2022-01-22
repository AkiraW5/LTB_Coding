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


def Use_ltb(opcao):

    subprocess.run('clear')
    print(C1 +
          "====================================================".center(width))
    print(C1 +
          "|                 LTB Options list                 |".center(width))
    print(C1 +
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


def Suggest(opcao):
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
            Suggest(opcao1)

        else:
            subprocess.run('clear')
            txt = 'ERROR: PLEASE TYPE A VALID OPTION'
            print(Back.BLACK + Fore.RED + '=' * width)
            print(Back.BLACK + Fore.RED + txt.center(width))
            print(Back.BLACK + Fore.RED + '=' * width)
            ctn = input(Fore.YELLOW + Back.BLACK +
                        'Type anything to continue: ')
            Suggest(opcao1)

        break


def Downloader(opcao):
    subprocess.run('clear')
    print(C1 +
          "====================================================".center(width))
    print(C1 +
          "|           Not avaliable yet! We're Sorry!        |".center(width))
    print(C1 +
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
            Downloader(opcao1)

        else:
            subprocess.run('clear')
            txt = 'ERROR: PLEASE TYPE A VALID OPTION'
            print(Back.BLACK + Fore.RED + '=' * width)
            print(Back.BLACK + Fore.RED + txt.center(width))
            print(Back.BLACK + Fore.RED + '=' * width)
            ctn = input(Fore.YELLOW + Back.BLACK +
                        'Type anything to continue: ')
            Downloader(opcao1)

        break


def GitHub_Page(opcao):
    subprocess.run('clear')
    print(C1 +
          "====================================================".center(width))
    print(C1 +
          "|            Hmm... Where did you get this?        |".center(width))
    print(C1 +
          "====================================================".center(width))
    print(C1 + "| Anyways, there you go! |".center(width))
    print(C1 + "| https://github.com/AkiraW5/LTB_Coding |".center(width))

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
            GitHub_Page(opcao1)

        else:
            subprocess.run('clear')
            txt = 'ERROR: PLEASE TYPE A VALID OPTION'
            print(Back.BLACK + Fore.RED + '=' * width)
            print(Back.BLACK + Fore.RED + txt.center(width))
            print(Back.BLACK + Fore.RED + '=' * width)
            ctn = input(Fore.YELLOW + Back.BLACK +
                        'Type anything to continue: ')
            GitHub_Page(opcao1)

        break


def size_box(msg):
    tam = len(msg)
    print('=' * tam)
    print(msg)
    print('=' * tam)


def menu(opcao):
    while opcao != '6':
        subprocess.run('clear')
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
        opcao = input(Fore.YELLOW + Back.BLACK + 'Type option: ')

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
