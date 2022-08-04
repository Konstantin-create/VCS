import sys
import os
from commands import *

# Get run args
args = sys.argv

# Functions
def main():
    """Function to parse args and call the function"""
    cwd = os.getcwd()
    if args[1].lower() == 'init':
        init = Init(cwd)


if __name__ == '__main__':
    main()


