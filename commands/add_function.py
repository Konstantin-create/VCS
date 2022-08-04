import os
import sys
import json
from colorama import init, Fore
from tools import get_all_files, is_exists


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
                    current_traking = json.load(file)
        
        if not (file_name == '-A' or file_name == '.'):
            if is_exists(self.run_path, file_name):
                if not (file_name in current_traking):
                    current_traking.append(file_name)
            else:
                print(Fore.RED + f'No such file in this folder(self.run_path)')
                sys.exit()
        else:
            current_traking = get_all_files(self.run_path)
        with open(self.traked_files_path, 'w') as file:
            print(current_traking)
            json.dump(current_traking, file, indent=4)
        
        print(Fore.GREEN + 'Files were successfully added to traked list')


    def is_traked_files_exists(self):
        return os.path.exists(self.run_path + '/.vcs')


