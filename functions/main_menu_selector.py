import sys
sys.path.append('../')
import os
from functions.common import clear, print_banner, print_version, local_command_execution
from classes.bcolors import bcolors

def main_menu_version():
    print(print_version())

def main_menu_help():
    begin, end = bcolors.GREEN, bcolors.END_C
    switcher_help = {
        "ghouls"    : '',
        "banner"    : 'Prints the banner for the program',
        "listeners" : '',
        "interact"  : '',
        "remove"    : '',
        "session"   : '',
        "use"       : '',
        "version"   : 'Prints the current version',
        "local"     : 'Enters into local terminal within program',
        "exit"      : '',
        "quit"      : '',
        "clear"     : 'Clears the terminal screen',
        "help"      : 'Prints the help main help menu' 
        }
        
    for key, value in switcher_help.items():
        print(begin + "{0:<10}".format(key) + end + " : {0:^10}".format(value))
    
    
    input("Press " + bcolors.BOLDER + "ENTER" + bcolors.END_C + " to continue...")


def main_menu_selection(choice):

    switcher = {
        "ghouls"    : lambda: "",
        "banner"    : lambda: input(bcolors.PURPLE + print_banner() + bcolors.END_C + "\nPress Enter..."),
        "listeners" : lambda: "",
        "interact"  : lambda: "",
        "remove"    : lambda: "",
        "session"   : lambda: "",
        "use"       : lambda: "",
        "version"   : lambda: input(bcolors.PURPLE + print_version() + bcolors.END_C + "\nPress Enter..."),
        "help"      : main_menu_help,
        "local"     : local_command_execution,
        "clear"     : clear,
        ""          : lambda: ""
    }

    # Get the function from switcher dictionary
    funct = switcher.get(choice, lambda: print(bcolors.ERROR + ' Invalid Choice ' + bcolors.END_C))
    # Execute the function
    return funct()
    