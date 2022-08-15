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
from datetime import datetime
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

    def create_commit(self, new_branch_name: str) -> dict:
        """Function to create first commit in a new branch"""

        files_to_found = []  # List of files which last version we find in commit tree
        changes = []  # List of last version hashes like [{'<filename_hash>': '<file_data_hash>'}, ...]
        for file in self.tracked_files:
            files_to_found.append(file[list(file.keys())[0]])
        current_commit = self.last_commit_hash

        while True:
            commit_info_path = f'{self.vcs_path}/commits/{self.current_branch}/{current_commit}/commit_info.json'
            if os.path.exists(commit_info_path):
                commit_info = json.load(open(commit_info_path, 'r'))

                for filename_to_find in files_to_found:
                    for bin_file in commit_info['changes']:
                        if filename_to_find in bin_file:
                            changes.append({filename_to_find: bin_file[filename_to_find]})
                            files_to_found.remove(filename_to_find)

            else:
                print(Fore.RED + 'Commit storage error')
                sys.exit()

            if commit_info['parent'] == self.current_branch:
                if len(files_to_found) != 0:
                    print(Fore.RED + 'Commit storage error')
                    print(Fore.RED + f'Elements {files_to_found} not found')
                    sys.exit()
                break
            current_commit = commit_info['parent']

        return {
            'message': f'Merged from {self.current_branch}',
            'changes': changes,
            'time_stamp': str(datetime.utcnow()),
            'parent': new_branch_name
        }
