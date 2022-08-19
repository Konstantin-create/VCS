"""
File of merge function
Functions:
    - Get state from branch and create merge commit in current branch and write this in file
"""

# Imports
import os
import sys
import json
from datetime import datetime
from colorama import init, Fore
from tools import last_commit_hash, get_branch_name, get_tracked_files, generate_hash

# Colorama init
init()


class Merge:
    """Class of merge command"""
    __slots__ = ('working_dir', 'vcs_path', 'last_commit_hash', 'current_branch', 'tracked_files')

    def __init__(self, working_dir: str):
        self.working_dir = working_dir
        self.vcs_path = f'{self.working_dir}/.vcs'
        self.last_commit_hash = last_commit_hash(self.working_dir)
        self.current_branch = get_branch_name(self.working_dir)
        self.tracked_files = get_tracked_files(self.working_dir)

    def merge(self, branch_name: str) -> None:
        """Function to merge branches"""

        # Check is branch name not current branch
        if branch_name == self.current_branch:
            print(Fore.RED + 'You cant merge current branch with the same branch')
            sys.exit()

        # Check is branches exists
        if self.is_branch_exists(branch_name):
            print(f'Branch {branch_name} is not found')
            sys.exit()
        if self.is_branch_exists(self.current_branch):
            print(f'Branch {branch_name} is not exists')
            sys.exit()

        commit_info = json.dumps(self.create_commit_info(branch_name), indent=4)
        commit_hash = generate_hash(str(commit_info).encode())
        os.mkdir(f'{self.vcs_path}/commits/{branch_name}/{commit_hash}')
        json.dump(commit_info, open(f'{self.vcs_path}/commits/{branch_name}/{commit_hash}/commit_info.json', 'w'))

    def create_commit_info(self, new_branch_name) -> dict:
        """Function to create commit info"""

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
            else:
                print(Fore.RED + 'Commit storage error')
                sys.exit()

            if commit_info['parent'] == self.current_branch:
                break
            current_commit = commit_info['parent']

        return {
            'message': f'Merged from {self.current_branch}',
            'changes': changes,
            'time_stamp': str(datetime.utcnow()),
            'parent': new_branch_name
        }

    def is_branch_exists(self, branch_name: str) -> bool:
        """Function to check is branch exists"""

        return os.path.exists(f'{self.vcs_path}/commits/{branch_name}')
