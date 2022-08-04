import os
import sys
import json
from colorama import init, Fore
from tools import get_all_files, is_exists, is_ignored, get_ignore


# Colorama init
init(autoreset=True)


class Add:
    __slots__ = ('run_path', 'traked_files_path')
    """Class to add file to traked files list"""
    def __init__(self, run_path):
        self.run_path = run_path
        self.traked_files_path = self.run_path + '/.vcs/traked_files.json'


    def add_traked_file(self, file_name: str) -> None:
        """Function to add file to traked list"""
        if not self.is_traked_files_exists():
            print(Fore.RED + '.vcs folder not found\nTry "vcs init"')
            return

        current_traking = []
        if os.path.exists(self.traked_files_path):
            with open(self.traked_files_path, 'r') as file:
                if file.read() != '':
                    current_traking = json.loads(file.read())
        
        if not (file_name == '-A' or file_name == '.'):
            if is_exists(self.run_path, file_name):
                if not (file_name in current_traking):
                    current_traking.append(file_name)
            else:
                print(Fore.RED + f'No such file in this folder(self.run_path)')
                sys.exit()
        else:
            current_traking = get_all_files(self.run_path)

        not_ignored_files = []
        ignore = get_ignore(self.run_path)
        if ignore:
            for file in current_traking:
                if not is_ignored(self.run_path, ignore, file):
                    not_ignored_files.append(file)
            print(Fore.GREEN + f'\nFound {len(ignore)} ignores')
        else:
            print(Fore.YELLOW + f'\nNo ignores foud!')

        with open(self.traked_files_path, 'w') as file:
            json.dump(not_ignored_files, file)

        print(f'{len(not_ignored_files)} were added to traked list')
        print(Fore.GREEN + 'Files were successfully added to traked list')


    def is_traked_files_exists(self) -> bool:
        """Function to check is .vcs exists"""
        return os.path.exists(self.run_path + '/.vcs')
    
    def traked_files_list(self):
        """Function to print list of current traked files"""
        if not self.is_traked_files_exists():
            print(Fore.RED + '.vcs folder not found\nTry "vcs init"')
            return

        if os.path.exists(self.traked_files_path):
            with open(self.traked_files_path, 'r') as file:
                if file.read() != '':
                    current_traking = json.loads(file.read())
            print('Traking files:')
            for file in current_traking:
                print(f'    {file}')
        else:
            print(Fore.YELLOW + 'No traking files. Use "vcs add <file_name | -A | .>"')
            return

