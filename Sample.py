# Required packages
import os

# The main function of this is to execute a command to clear your terminal based on the name in it
def Terminal_Cleaner():
    if os.name == "posix":
        os.system('clear')
    else:
        os.system('cls')
