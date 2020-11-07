"""
Commonly Called Functions
"""
## Imports ##
import sys
sys.path.append('../')

from classes.common import cd
import os

def print_banner():
  return (
"""
  ▄████  ██░ ██  ▒█████   █    ██  ██▓    
 ██▒ ▀█▒▓██░ ██▒▒██▒ ███▒ ██  ▓██▒▓██▒    
▒██░▄▄▄░▒██▀▀██░▒██░█ ██▒▓██  ▒██░▒██░    
░▓█  ██▓░▓█ ░██ ▒███  ██░▓▓█  ░██░▒██░    
░▒▓███▀▒░▓█▒░██▓░ ████▓▒░▒▒█████▓ ░██████▒
 ░▒   ▒  ▒ ░░▒░▒░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ░ ▒░▓  ░
  ░   ░  ▒ ░▒░ ░  ░ ▒ ▒░ ░░▒░ ░ ░ ░ ░ ▒  ░
░ ░   ░  ░  ░░ ░░ ░ ░ ▒   ░░░ ░ ░   ░ ░   
      ░  ░  ░  ░    ░ ░     ░         ░  ░
""")

def print_version():
  return "Version 1.0.0"
  
def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

def local_command_execution():
  
  while True:
    current_working_dir = os.getcwd()
    local_command = input(f"<{current_working_dir}>>> ")
    if local_command.lower() not in ["exit", "quit"]:
      if local_command.split(" ")[0] == "cd":
        try: os.chdir(local_command.split("cd ")[1] + "\\")
        except FileNotFoundError: continue
        except OSError: continue
      
      os.system(local_command)
    else:
      break
  
