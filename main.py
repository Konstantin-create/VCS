import os
import sys
from commands import *
from colorama import init, Fore


# Colorama init
init(autoreset=True)

# Get run args
args = sys.argv

# Functions
def main():
    """Function to parse args and call the function"""
    cwd = os.getcwd()
    if args[1].lower() == 'init':
        if len(args) >= 3 and args[2].lower() == '-b':
            init = Init(cwd, base_branch=args[3])
        else:
            init = Init(cwd)
    elif args[1].lower() == 'add':
        if len(args) >= 3:
            add = Add(cwd)
        else:
            print(Fore.RED + 'Not enough arguments! Use "vcs add --help"')


if __name__ == '__main__':
    main()


