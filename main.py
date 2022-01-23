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


def snake():
    speed = 15

    #windows sizes

    frame_size_x = 1380
    frame_size_y = 840

    check_errors = pygame.init()

    if (check_errors[1] > 0):
        print("Error ", check_errors[1])
    else:
        print("Game Succesfully initialized")

    #initialise game window

    pygame.display.set_caption("Snake Game")
    game_window = pygame.display.set_mode((frame_size_x, frame_size_y))

    # colors
    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    blue = pygame.Color(0, 0, 255)

    fps_controller = pygame.time.Clock()
    # one snake square size
    square_size = 60

    def init_vars():
        global head_pos, snake_body, food_pos, food_spawn, score, direction
        direction = "RIGHT"
        head_pos = [120, 60]
        snake_body = [[120, 60]]
        food_pos = [
            random.randrange(1, (frame_size_x // square_size)) * square_size,
            random.randrange(1, (frame_size_y // square_size)) * square_size
        ]
        food_spawn = True
        score = 0

    init_vars()

    def show_score(choice, color, font, size):
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render("Score: " + str(score), True, color)
        score_rect = score_surface.get_rect()
        if choice == 1:
            score_rect.midtop = (frame_size_x / 10, 15)
        else:
            score_rect.midtop = (frame_size_x / 2, frame_size_y / 1.25)

        game_window.blit(score_surface, score_rect)

    #game loop

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_UP
                        or event.key == ord("w") and direction != "DOWN"):
                    direction = "UP"
                elif (event.key == pygame.K_DOWN
                      or event.key == ord("s") and direction != "UP"):
                    direction = "DOWN"
                elif (event.key == pygame.K_LEFT
                      or event.key == ord("a") and direction != "RIGHT"):
                    direction = "LEFT"
                elif (event.key == pygame.K_RIGHT
                      or event.key == ord("d") and direction != "LEFT"):
                    direction = "RIGHT"

            if direction == "UP":
                head_pos[1] -= square_size
            elif direction == "DOWN":
                head_pos[1] += square_size
            elif direction == "LEFT":
                head_pos[0] -= square_size
            else:
                head_pos[0] += square_size

            if head_pos[0] < 0:
                head_pos[0] = frame_size_x - square_size
            elif head_pos[0] > frame_size_x - square_size:
                head_pos[0] = 0
            elif head_pos[1] < 0:
                head_pos[1] = frame_size_y - square_size
            elif head_pos[1] > frame_size_y - square_size:
                head_pos[1] = 0

            #eating apple
            snake_body.insert(0, list(head_pos))
            if head_pos[0] == food_pos[0] and head_pos[1] == food_pos[1]:
                score += 1
                food_spawn = False
            else:
                snake_body.pop()

            # spawn food
            if not food_spawn:
                food_pos = [
                    random.randrange(1, (frame_size_x // square_size)) *
                    square_size,
                    random.randrange(1, (frame_size_y // square_size)) *
                    square_size
                ]
                food_spawn = True

            # GFX
            game_window.fill(black)
            for pos in snake_body:
                pygame.draw.rect(
                    game_window, green,
                    pygame.Rect(pos[0] + 2, pos[1] + 2, square_size - 2,
                                square_size - 2))

            pygame.draw.rect(
                game_window, red,
                pygame.Rect(food_pos[0], food_pos[1], square_size,
                            square_size))

            # game over condiditons

            for block in snake_body[1:]:
                if head_pos[0] == block[0] and head_pos[1] == block[1]:
                    init_vars()

            show_score(1, white, 'consolas', 20)
            pygame.display.update()
            fps_controller.tick(speed)


def Use_ltb(option):

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

    option1 = input(Fore.YELLOW + Back.BLACK + 'Type option: ')

    while option1 != '0':

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
            txt = 'ERROR: YOU NEED SELECT SOME OPTION'
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
            txt = 'ERROR: YOU NEED SELECT SOME OPTION'
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
            txt = 'ERROR: YOU NEED SELECT SOME OPTION'
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
    while option != '7':
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

        elif option == '7':
            snake()

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