"""
File of ignore command
Functions:
    - Create custom ignore file
    - Get ignore file data
"""

# Imports
import os
from tools import get_ignore, get_ignore_template, templates
from colorama import init, Fore

# Colorama init
init(autoreset=True)


class Ignore:
    """Class for manage .ignore file"""
    __slots__ = ('working_dir', 'base_ignores')

    def __init__(self, working_dir):
        self.working_dir = working_dir
        self.base_ignores = '# Base ignores\n/.git\n/.vcs/\n'

    def create_file(self, template: str = False) -> None:
        """Function to check is .ignore exists"""

        if os.path.exists(f'{self.working_dir}/.ignore'):
            command = str(input(Fore.YELLOW + '.ignore file is already exists. Rewrote?\ny/N: '))
            if 'n' in command:
                return
            print()
        print(Fore.GREEN + f'.ignore file with base exceptions was created successfully')
        self.set_base_ignores()
        if template:
            self.add_template_ignore(template)

    def set_base_ignores(self) -> None:
        """Function to set some base ignores(like .git, .vcs, ect...)"""

        with open(f'{self.working_dir}/.ignore', 'w') as file:
            file.write(self.base_ignores)

    def get_ignore_list(self) -> None:
        """Function to get list of ignores from .ignore"""

        ignores = get_ignore(self.working_dir)
        if ignores is None:
            print(Fore.RED + '.ignore file not found. Try "vcs ignore -n | --new" to create this')
            return
        if len(ignores):
            print(Fore.YELLOW + 'No ignores found')
        print('Ignores:')
        print('  ' + '\n  '.join(ignores))
        print()
        print(Fore.GREEN + f'Total {len(ignores)} ignores foud')

    def add_template_ignore(self, template: str) -> None:
        """Function to add template to .ignore"""

        if os.path.exists(f'{self.working_dir}/.ignore'):
            self.set_base_ignores()
        template_data = get_ignore_template(template)
        if not template_data:
            print(Fore.RED + f'No such template: {template}')
        with open(f'{self.working_dir}/.ignore', 'a') as file:
            file.write(f'{template_data}\n')

    def get_template_list(self) -> None:
        """Function to get templates list"""

        print('Ignore templates list:')

        print('  ' + '\n  '.join(list(templates.keys())))
        print(f'\nTotal {len(list(templates.keys()))} templates found')
