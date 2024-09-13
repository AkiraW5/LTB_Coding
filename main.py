import os
import subprocess
import platform
import getpass
from colorama import Fore, Back, init

# Inicializar o colorama
init(autoreset=True)

# Variáveis de configuração
width = os.get_terminal_size().columns
version = platform.version()
release = platform.release()
machine = platform.machine()
username = getpass.getuser()

# Funções de impressão
def clear_screen():
    """Limpa a tela dependendo do sistema operacional."""
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

def print_centered_message(msg, color=Fore.WHITE):
    """Imprime uma mensagem centralizada com cor opcional."""
    print(color + msg.center(width))

def print_separator(char='─', length=None, color=Fore.CYAN):
    """Imprime uma linha de separação com o caractere especificado e cor."""
    print(color + char * (length or width))

def print_error_message(msg):
    """Imprime uma mensagem de erro."""
    clear_screen()
    print_separator('=', color=Fore.RED)
    print_centered_message(msg, Fore.RED)
    print_separator('=', color=Fore.RED)

def print_message(title, lines, footer):
    """Imprime uma mensagem com título, linhas e rodapé."""
    clear_screen()
    print_centered_message(title, Fore.CYAN)
    print_separator()
    for line in lines:
        print_centered_message(line)
    print_separator()
    print_centered_message(footer, Fore.YELLOW)
    input(Fore.YELLOW + Back.BLACK + 'Type option: ')

# Funções de menu
def print_refined_menu():
    """Imprime o menu principal com refinamentos."""
    clear_screen()
    # Cabeçalho com bordas estilizadas
    print(Fore.CYAN + "┌" + "─" * (width - 2) + "┐")
    print_centered_message(f"LINUX TOOLBOX 0.1  | {machine} | USER: {username.upper()}", Fore.CYAN)
    print_centered_message(f"YOUR CURRENT SO: {release} | VERSION: {version}", Fore.CYAN)
    print(Fore.CYAN + "└" + "─" * (width - 2) + "┘")
    
    # Mensagem de boas-vindas
    print_centered_message("=" + "Howdy Folks! Welcome to LTB!".center(width - 2) + "=", Fore.YELLOW)
    print_separator()

    # Opções do menu
    options = [
        "Now, what you wanna do?",
        Fore.GREEN + "1- Let's use LTB!",
        Fore.GREEN + "2- Want to suggest us something?",
        Fore.GREEN + "3- Downloader (BETA)",
        Fore.GREEN + "4- Look our Github page!",
        Fore.GREEN + "5- What's LTB?",
        Fore.RED + "6- Let me out! (quit)"
    ]
    for option in options:
        print_centered_message(option)
    
    print_separator(Fore.CYAN)

def handle_option(option):
    """Manipula a opção selecionada pelo usuário."""
    options = {
        '1': lambda: print_message("LTB Options list", ["No options available"], '0- Back to menu'),
        '2': lambda: print_message("Oh, so you have a suggestion?", [
            "Nice to hear! Sadly, Due to lack of experience, we",
            "can't add this now! But you can contact us in TG!",
            "@krebox @akirawa1"
        ], '0- Back to menu'),
        '3': lambda: print_message("Not available yet! We're Sorry!", [], '0- Back to menu'),
        '4': lambda: print_message("Hmm... Where did you get this?", [
            "Anyways, there you go!",
            "https://github.com/AkiraW5/LTB_Coding"
        ], '0- Back to menu'),
        '5': lambda: print_message("LTB is a toolbox app for Linux...", [], '0- Back to menu'),
        '6': exit
    }
    if option == '0':
        return True  # Indica que deve retornar ao menu principal
    else:
        action = options.get(option)
        if action:
            action()
        else:
            print_error_message('ERROR: PLEASE TYPE A VALID OPTION')
            input(Fore.YELLOW + Back.BLACK + 'Type anything to continue: ')
        return False  # Indica que deve continuar no loop

# Iniciar o menu
while True:
    print_refined_menu()
    option = input(Fore.YELLOW + Back.BLACK + 'Type option: ')
    if handle_option(option):
        continue  # Retorna ao menu principal
