## IMPORTS ##
from functions.main_menu_selector import main_menu_selection
from functions.common import clear, print_banner, print_version
from classes.bcolors import bcolors
import sys
import os

if __name__ == "__main__":
    # Clear terminal
    clear()
    # Print Banner and Version on start of program
    print(bcolors.GREEN + print_banner() + bcolors.END_C)
    print(bcolors.BOLDER + bcolors.GREEN + print_version() + bcolors.END_C)

    while True:
        # Get choice input from user - This will be fed to a function that will use a case/switch method
        choice = input( bcolors.PURPLE + "<GHOUL_TERMINAL>>> " + bcolors.END_C)
        main_menu_selection(choice) if choice not in ['quit', 'exit'] else sys.exit(0)