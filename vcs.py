import os
import sys
from tools import is_vcs_initialized
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
    else:
        if not is_vcs_initialized(cwd):
            print(Fore.RED + 'VCS is not initialized try "vcs init"')
            sys.exit()
        if args[1].lower() == 'add':
            if len(args) >= 3:
                add = Add(cwd)
                if args[2] == '-l' or args[2] == '--list':
                    add.tracked_files_list()
                else:
                    add.add_tracked_file(args[2])

            else:
                print(Fore.RED + 'Not enough arguments! Use "vcs add --help"')
        elif args[1].lower() == 'commit':
            commit = Commit(cwd)
            commit.commit('Init commit')


if __name__ == '__main__':
    main()
