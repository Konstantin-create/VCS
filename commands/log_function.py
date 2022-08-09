"""
File of log command
Functions:
    - Print last commit info by id
    - Print commit info by hash
"""

# Imports
import os
import json
from colorama import init, Fore
from tools import last_commit_hash, get_branch_name

# Colorama init
init(autoreset=True)

class Log:
    """Class of log command"""

    def __init__(self, working_dir: str):
        self.working_dir = working_dir

    def get_commit_info(self, commit_hash: str = '') -> None:
        if commit_hash == '':
            if not last_commit_hash(self.working_dir):
                print(Fore.RED + 'You have no commits in this dir')
                return
            if os.path.exists(f'{self.working_dir}/.vcs/commits/{get_branch_name(self.working_dir)}/{last_commit_hash(self.working_dir)}/commit_info.json'):
                with open(f'{self.working_dir}/.vcs/commits/{get_branch_name(self.working_dir)}/{last_commit_hash(self.working_dir)}/commit_info.json', 'r') as file:
                    commit_info = json.load(file)
                print(f'Commit: {last_commit_hash(self.working_dir)}')
                print(f'Message: {commit_info["message"]}')
                print(f'Time stamp: {commit_info["time_stamp"]}')
                print(f'Parent: {commit_info["parent"]}')
                print()
