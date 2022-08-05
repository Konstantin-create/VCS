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
            if args[2] == '-l' or args[2] == '--list':
                add.tracked_files_list()
            else:
                add.add_tracked_file(args[2])

        else:
            print(Fore.RED + 'Not enough arguments! Use "vcs add --help"')


if __name__ == '__main__':
    main()
