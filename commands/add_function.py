import os
import json
from colorama import init, Fore
from tools import get_all_files


# Colorama init
init(autoreset=True)


class Add:
    """Class to add file to traked files list"""
    def __init__(self, run_path):
        self.run_path = run_path
        self.traked_files_path = self.run_path + '.vcs/traked_files'


    def add_traked_file(self, file_name: str) -> None:
        """Function to add file to traked list"""
        if not self.is_traked_files_exists():
            print(Fore.RED + '.vcs folder not found\nTry "vcs init"')
            return

        current_traking = []
        if os.path.exists(self.traked_files_path):
            with open(self.traked_files_path, 'r') as file:
                current_traking = json.load(file)
        
        if file_name != '-A' or file_name != '.':
            current_traking.append(file_name)
        else:
            current_traking += get_all_files(self.run_path)
        with open(self.traked_files_path, 'w') as file:
            json.dump(current_traking, file)
        
        print(Fore.GREEN + 'Files were successfully added to traked list')


    def is_traked_files_exists(self):
        return os.path.exists(self.run_path + '.vcs')


