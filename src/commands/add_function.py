"""
File of add command
Functions:
    - Create tracked files list
    - Append items in tracked files list
    - Remove items in tracked files list
    - Print tracked files list
"""

# Imports
import os
import sys
import json
from colorama import init, Fore
from tools import get_all_files, is_exists, is_ignored, get_ignore, generate_hash, is_vcs_initialized

# Colorama init
init(autoreset=True)


class Add:
    """Class to manage tracked files list"""
    __slots__ = ('run_path', 'tracked_files_path', 'verbose', 'force')

    def __init__(self, run_path) -> None:
        self.run_path = run_path
        self.tracked_files_path = self.run_path + '/.vcs/tracked_files.json'
        self.verbose = False
        self.force = False

    def add_tracked_file(self, file_name: str, verbose: bool, force: bool) -> None:
        """Function to add file to tracked list"""
        if not is_vcs_initialized(self.run_path):
            print(Fore.RED + '.vcs folder not found\nTry "vcs init"')
            return

        self.verbose = verbose
        self.force = force

        current_tracking = []
        if os.path.exists(self.tracked_files_path):
            with open(self.tracked_files_path, encoding='utf-8') as file:
                file_data = file.read()
                if len(file_data):
                    for file in json.load(open(self.tracked_files_path)):
                        current_tracking.append(list(file.keys())[0])

        if not (file_name == '-A' or file_name == '.'):
            if is_exists(self.run_path, file_name):
                if not (file_name in current_tracking):
                    current_tracking.append(file_name)
            else:
                print(Fore.RED + f'No such file in this folder({self.run_path}/{file_name})')
                sys.exit()
        else:
            current_tracking = get_all_files(self.run_path)

        not_ignored_files = []
        if not self.force:
            ignore = get_ignore(self.run_path)
            if ignore:
                for file in current_tracking:
                    if not is_ignored(ignore, file) and is_exists(self.run_path, file):
                        not_ignored_files.append({file: generate_hash(file.encode())})
                print(Fore.GREEN + f'\nFound {len(ignore)} ignores')
            else:
                print(Fore.YELLOW + f'\nNo ignores found!')
                for file in current_tracking:
                    not_ignored_files.append({file: generate_hash(file.encode())})
        else:
            print(Fore.YELLOW + 'Force mode. .ignore file will not be read')
            for file in current_tracking:
                not_ignored_files.append({file: generate_hash(file.encode())})

        with open(self.tracked_files_path, 'w') as file:
            json.dump(not_ignored_files, file, indent=4)

        if self.verbose:
            pretty_added_files = ''
            for file in not_ignored_files:
                pretty_added_files += f'    {list(file.keys())[0]} - {file[list(file.keys())[0]]}\n'
            print(f'Added files:\n{pretty_added_files}')
        print(f'{len(not_ignored_files)} were added to tracked list')
        print(Fore.GREEN + 'Files were successfully added to tracked list')

    def tracked_files_list(self) -> None:
        """Function to print list of current tracked files"""
        if os.path.exists(self.tracked_files_path):
            with open(self.tracked_files_path, 'r', encoding='utf-8') as file:
                if len(file.read()):
                    current_tracking = json.load(open(self.tracked_files_path))
            print('Tracked files:')
            for file in current_tracking:
                print(f'    {list(file.keys())[0]}')
        else:
            print(Fore.YELLOW + 'No tracking files. Use "vcs add <file_name | -A | .>"')
            return

    def tracked_files_clean(self) -> None:
        """Function to clean tracked files list"""
        if not is_vcs_initialized(self.run_path):
            print(Fore.RED + '.vcs folder not found\nTry "vcs init"')
            return
        with open(self.tracked_files_path, 'w') as file:
            file.write('[]')
        print(Fore.GREEN + '\nTracked files have been cleared')
