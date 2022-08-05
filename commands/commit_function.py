import os
import sys
import json
from tools import generate_hash
from colorama import init, Fore

# Colorama init
init(autoreset=True)


class Commit:
    def __init__(self, working_dir: str):
        self.working_dir = working_dir
        self.vcs_path = working_dir + '/.vcs'

    def commit(self, message):
        self.get_files_list()

    def get_files_list(self):
        """Function to get tracked list"""
        if os.path.exists(self.vcs_path + '/tracked_files.json'):
            tracked_files = json.load(open(self.vcs_path + '/tracked_files.json'))
            for file in tracked_files:
                print(self.get_file_hash(file)) 
            return
        print(Fore.RED + 'No tracked files!')
        print('    Try "vcs add ."')
        sys.exit()

    def get_file_hash(self, file_path: str) -> str:
        if os.path.exists(self.working_dir + file_path):
            print(file_path)
            with open(self.working_dir + file_path, 'rb') as file:
                file_data = file.read()
            return generate_hash(file_data)
        else:
            print(Fore.RED + f'No such file {file_name}\n   Try "vcs add ." command')
    


    def get_last_commit(self) -> list:
        last_hash = self.get_last_hash()
        if not last_hash:
            if os.path.exists(self.vcs_path + '/objects/'+ self.branch_name() + last_hash):
                pass

    def get_last_hash(self) -> str | None:
        """Function to get last commit hash"""
        if os.path.exists(self.vcs_path+'/LAST_COMMIT'):
            with open(self.vcs_path + '/LAST_COMMIT') as file:
                file_data =  file.read()
            return file_data

    def branch_name(self) -> str | None:
        if os.path.exists(self.vcs_path + '/config.json'):
            branch_name = json.load(open(self.vcs_path + '/.config'))
            return branch_name
    
    def check_vcs_path(self) -> bool:
        """Function to check is .vcs is initialized"""
        return os.path.exists(self.vcs_path)
    
