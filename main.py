# Made by Kitten Team in Brazil :)
import subprocess
from ast import Store
from operator import rshift
import os

os.system("pip install pygame")
os.system("pip install colorama"
          )  #install colorama module as long as your don't have it

import colorama
from colorama import Fore, Back, Style
import platform
import getpass
import socket
import csv
import pygame, sys, time, random

print('test')

colorama.init(
    autoreset=True)  #initialize the colorama module and enable the autoreset

# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET. = all possible colors for the letters
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET. = all possible colors to the background
# Style: DIM, NORMAL, BRIGHT, RESET_ALL = all possible styles for the letters

C = Fore.BLUE + Back.BLACK  #uses color combination: black for the background and blue to the letters
C1 = Fore.GREEN + Back.BLACK  #uses color combination: black for the background and green to the letters

width = os.get_terminal_size().columns  #get the size of your terminal

version = platform.version()  #get your system version
release = platform.release()  #get your system name
machine = platform.machine()  #get arch do your machine
GetUser = getpass.getuser()  #get your username
UserInf = Back.BLACK + 'LINUX TOOLBOX' + Fore.BLUE + ' 0.1 ' + Fore.WHITE + ' | ' + Fore.BLUE + machine + Fore.WHITE + ' | ' + 'USER: ' + Fore.YELLOW + GetUser.upper(
) + Fore.WHITE + ' | '
UserInf2 = Back.BLACK + 'YOUR CURRENT SO: ' + Fore.GREEN + release + Fore.WHITE + ' | ' + 'VERSION: ' + Fore.GREEN + version + Fore.WHITE + ' | '
# UserInf and UserInf2 set the informations assigned above

option = 0  #s Set empty value for option


def Use_ltb(option):

    subprocess.run('clear')
    print(C1 +
          "====================================================".center(width))
    print(C1 +
          "|                 LTB Options list                 |".center(width))
    print(C1 +
          "====================================================".center(width))

    print("nao tem nada".center(width))

    print(Back.BLACK + '-' * width)
    print(Back.BLACK + Fore.RED + '0- ' + Fore.GREEN + 'Back to menu')
    print(Back.BLACK + '-' * width)

    option1 = input(Fore.YELLOW + Back.BLACK + 'Type option: ')

    while option1 != '0':

        if option1 == '0':
            menu(option1)
        elif option1 < '0':
            subprocess.run('clear')
            txt = 'ERROR: YOU NEED SELECT AN OPTION'
            print(Back.BLACK + Fore.RED + '=' * width)
            print(Back.BLACK + Fore.RED + txt.center(width))
            print(Back.BLACK + Fore.RED + '=' * width)
            ctn = input(Fore.YELLOW + Back.BLACK +
                        'Type anything to continue: ')
            Use_ltb(option1)

        else:
            subprocess.run('clear')
            txt = 'ERROR: PLEASE TYPE A VALID OPTION'
            print(Back.BLACK + Fore.RED + '=' * width)
            print(Back.BLACK + Fore.RED + txt.center(width))
            print(Back.BLACK + Fore.RED + '=' * width)
            ctn = input(Fore.YELLOW + Back.BLACK +
                        'Type anything to continue: ')
            Use_ltb(option1)

        break


# Use ltb is the equivalent to the first menu option


def Suggest(option):
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

    option1 = input(Fore.YELLOW + Back.BLACK + 'Type option: ')

    while option1 != '0':

        if option == '0':
            menu(option1)

        elif option1 < '0':
            subprocess.run('clear')
            txt = 'ERROR: YOU NEED SELECT AN OPTION'
            print(Back.BLACK + Fore.RED + '=' * width)
            print(Back.BLACK + Fore.RED + txt.center(width))
            print(Back.BLACK + Fore.RED + '=' * width)
            ctn = input(Fore.YELLOW + Back.BLACK +
                        'Type anything to continue: ')
            Suggest(option1)

        else:
            subprocess.run('clear')
            txt = 'ERROR: PLEASE TYPE A VALID OPTION'
            print(Back.BLACK + Fore.RED + '=' * width)
            print(Back.BLACK + Fore.RED + txt.center(width))
            print(Back.BLACK + Fore.RED + '=' * width)
            ctn = input(Fore.YELLOW + Back.BLACK +
                        'Type anything to continue: ')
            Suggest(option1)

        break


# Suggest is the equivalent to the second menu option


def Downloader(option):
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

    option1 = input(Fore.YELLOW + Back.BLACK + 'Type option: ')

    while option1 != '0':

        if option1 == '0':
            menu(option1)

        elif option1 < '0':
            subprocess.run('clear')
            txt = 'ERROR: YOU NEED SELECT AN OPTION'
            print(Back.BLACK + Fore.RED + '=' * width)
            print(Back.BLACK + Fore.RED + txt.center(width))
            print(Back.BLACK + Fore.RED + '=' * width)
            ctn = input(Fore.YELLOW + Back.BLACK +
                        'Type anything to continue: ')
            Downloader(option1)

        else:
            subprocess.run('clear')
            txt = 'ERROR: PLEASE TYPE A VALID OPTION'
            print(Back.BLACK + Fore.RED + '=' * width)
            print(Back.BLACK + Fore.RED + txt.center(width))
            print(Back.BLACK + Fore.RED + '=' * width)
            ctn = input(Fore.YELLOW + Back.BLACK +
                        'Type anything to continue: ')
            Downloader(option1)

        break


# Downloader is the equivalent to the third menu option


def GitHub_Page(option):
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

    option1 = input(Fore.YELLOW + Back.BLACK + 'Type option: ')

    while option1 != '0':

        if option1 == '0':
            menu(option1)

        elif option1 < '0':
            subprocess.run('clear')
            txt = 'ERROR: YOU NEED SELECT AN OPTION'
            print(Back.BLACK + Fore.RED + '=' * width)
            print(Back.BLACK + Fore.RED + txt.center(width))
            print(Back.BLACK + Fore.RED + '=' * width)
            ctn = input(Fore.YELLOW + Back.BLACK +
                        'Type anything to continue: ')
            GitHub_Page(option1)

        else:
            subprocess.run('clear')
            txt = 'ERROR: PLEASE TYPE A VALID OPTION'
            print(Back.BLACK + Fore.RED + '=' * width)
            print(Back.BLACK + Fore.RED + txt.center(width))
            print(Back.BLACK + Fore.RED + '=' * width)
            ctn = input(Fore.YELLOW + Back.BLACK +
                        'Type anything to continue: ')
            GitHub_Page(option1)

        break


# GitHub Page is the equivalent to the forth menu option


def size_box(msg):
    tam = len(msg)
    print('=' * tam)
    print(msg)
    print('=' * tam)


# Size box automatically creates a size box depending on the text


def menu(option):
    while option != '6':
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
        option = input(Fore.YELLOW + Back.BLACK + 'Type option: ')

        if option == '1':
            Use_ltb(option)

        elif option == '2':
            Suggest(option)

        elif option == '3':
            Downloader(option)

        elif option == '4':
            GitHub_Page(option)

        elif option == '5':
            print('5')
            break

        elif option == '6':
            quit

        elif option < '0':
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


# The menu function create the main menu using the above functions

menu(option)