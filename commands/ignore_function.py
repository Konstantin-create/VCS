"""
File of ignore command
Functions:
    - Create custom ignore file
    - Get ignore file data
"""

# Imports
import os
from colorama import init, Fore

# Colorama init
init(autoreset=True)

class Ignore:
    """Class for manage .ignore file"""

    def __init__(self, working_dir):
        self.working_dir = working_dir
        self.base_ignores = '# Base ignores\n/.git\n/.vcs/\n'
    
    def create_file(self) -> None:
        """Function to check is .ignore exists"""
        if os.path.exists(f'{self.working_dir}/.ignore'):
            command = str(input(Fore.YELLOW + '.ignore file is already exists. Rewrote?\ny/N: '))
            if 'n' in command:
                return
            print()
        print(Fore.GREEN + f'.ignore file with base exceptions was created successfully')
        self.set_base_ignores()

    def set_base_ignores(self) -> None:
        """Function to set some base ignores(like .git, .vcs, ect...)"""
        with open(f'{self.working_dir}/.ignore', 'w') as file:
            file.write(self.base_ignores)

