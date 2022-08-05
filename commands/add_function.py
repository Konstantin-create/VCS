import os
import sys
import json
from colorama import init, Fore
from tools import get_all_files, is_exists, is_ignored, get_ignore

# Colorama init
init(autoreset=True)


class Add:
    __slots__ = ('run_path', 'tracked_files_path')
    """Class to add file to tracked files list"""

    def __init__(self, run_path):
        self.run_path = run_path
        self.tracked_files_path = self.run_path + '/.vcs/tracked_files.json'

    def add_tracked_file(self, file_name: str) -> None:
        """Function to add file to tracked list"""
        if not self.is_tracked_files_exists():
            print(Fore.RED + '.vcs folder not found\nTry "vcs init"')
            return

        current_traking = []
        if os.path.exists(self.tracked_files_path):
            with open(self.tracked_files_path, encoding='utf-8') as file:
                file_data = file.read()
                if len(file_data):
                    current_traking = json.load(open(self.tracked_files_path))

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

        with open(self.tracked_files_path, 'w') as file:
            json.dump(not_ignored_files, file)

        print(f'{len(not_ignored_files)} were added to tracked list')
        print(Fore.GREEN + 'Files were successfully added to tracked list')

    def is_tracked_files_exists(self) -> bool:
        """Function to check is .vcs exists"""
        return os.path.exists(self.run_path + '/.vcs')

    def tracked_files_list(self):
        """Function to print list of current tracked files"""
        if not self.is_tracked_files_exists():
            print(Fore.RED + '.vcs folder not found\nTry "vcs init"')
            return

        if os.path.exists(self.tracked_files_path):
            with open(self.tracked_files_path, 'r', encoding='utf-8') as file:
                if len(file.read()):
                    current_traking = json.load(open(self.tracked_files_path))
            print('Traking files:')
            for file in current_traking:
                print(f'    {file}')
        else:
            print(Fore.YELLOW + 'No traking files. Use "vcs add <file_name | -A | .>"')
            return
