"""
File of checkout function
Functions:
    - Create new branch
    - Switch branches
"""

# Imports
import os
import sys
import json
from colorama import init, Fore
from tools import get_branch_name, last_commit_hash, get_tracked_files

# Colorama init
init(autoreset=True)


class CheckOut:
    """Function of checkout command"""

    def __init__(self, working_dir: str):
        self.working_dir = working_dir
        self.vcs_path = f'{self.working_dir}/.vcs'
        self.current_branch = get_branch_name(self.working_dir)
        self.last_commit_hash = last_commit_hash(self.working_dir)
        self.tracked_files = get_tracked_files(self.working_dir)

    def checkout(self, branch_name: str = '') -> None:
        """Function to switch branch"""

        if branch_name == self.current_branch:
            print(Fore.YELLOW + f'Already on {branch_name}')
            sys.exit()
        self.change_current_branch(branch_name)

    def is_branch_exists(self, branch_name: str) -> bool:
        """Function to check is branch exists"""

        return os.path.exists(f'{self.vcs_path}/commits/{branch_name}')

    def change_current_branch(self, branch_name: str) -> None:
        """Function to set current branch name"""

        # Edit CURRENT_BRANCH
        with open(f'{self.vcs_path}/CURRENT_BRANCH', 'w') as file:
            file.write(branch_name)

        # Edit
        config_data = {}
        if os.path.exists(f'{self.vcs_path}/config.json'):
            config_data = json.load(open(f'{self.vcs_path}/config.json', 'r'))
        config_data[branch_name] = ''  # Todo edit commit hash
        json.dump(config_data, open(f'{self.vcs_path}/config.json', 'w'))

        os.mkdir(f'{self.vcs_path}/commits/{branch_name}')

    def create_commit(self) -> dict:
        """Function to create first commit in a new branch"""

        files_to_found = self.tracked_files  # List of files which last version we find in commit tree
        current_commit = self.last_commit_hash
        while True:
            commit_info_path = f'{self.vcs_path}/commits/{self.current_branch}/{current_commit}/commit_info.json'
            if os.path.exists(commit_info_path):
                commit_info = json.load(open(commit_info_path, 'r'))
