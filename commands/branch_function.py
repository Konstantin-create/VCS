"""
File of branch command
Function:
    - Create new branch
    - Rename branch
"""

# Imports
import os
import sys
import json
import shutil
from datetime import datetime
from colorama import init, Fore
from tools import generate_hash
from tools import get_branch_name, get_branches
from tools import last_commit_hash, get_tracked_files

# Colorama init
init(autoreset=True)


class Branch:
    """Class to manage branches"""

    def __init__(self, working_dir: str):
        self.working_dir = working_dir
        self.vcs_path = f'{self.working_dir}/.vcs'
        self.current_branch = get_branch_name(self.working_dir)
        self.branches = get_branches(self.working_dir)
        self.last_commit_hash = last_commit_hash(self.working_dir)
        self.tracked_files = get_tracked_files(self.working_dir)

    def create_new(self, branch_name: str) -> None:
        """Function to create new branch"""

        if not self.is_branch_exists(branch_name):
            commit_info = self.create_commit_info(branch_name)
            commit_hash = generate_hash(str(commit_info).encode())
            self.write_changes(branch_name, commit_info, commit_hash)
            print(Fore.GREEN + f'Branch {branch_name} has been created')
            print(f'{len(commit_info["changes"])} files were inherited')
        else:
            print(Fore.RED + f'Branch {branch_name} is already exists')
            sys.exit()

    def branches_list(self):
        """Function to print list of branches"""

        print('Branches:')
        print('  ' + '\n  '.join(self.branches))
        print()
        print(f'Total {len(self.branches)} branches')

    def remove_branch(self, branch_name: str) -> None:
        """Function to remove branch"""

        if len(branch_name) <= 1:
            print(Fore.YELLOW + 'You can\'t remove the last branch')
            sys.exit()
        if self.current_branch == branch_name:
            print(Fore.YELLOW + 'You can\'t delete the branch you are currently on')
            sys.exit()
        if not self.is_branch_exists(branch_name):
            print(Fore.RED + f'Branch {branch_name} not found')
            sys.exit()

        shutil.rmtree(f'{self.vcs_path}/commits/{branch_name}')
        current_config = json.load(open(f'{self.vcs_path}/config.json', 'r'))
        if branch_name in current_config:
            current_config.pop(branch_name)
            json.dump(current_config, open(f'{self.vcs_path}/config.json', 'w'))
        print(f'Branch {branch_name} was successfully deleted')

    def is_branch_exists(self, branch_name: str) -> bool:
        """Function check is branch exists"""

        return os.path.exists(f'{self.vcs_path}/commits/{branch_name}')

    def create_commit_info(self, new_branch_name: str) -> dict:
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
            else:
                print(Fore.RED + 'Commit storage error')
                sys.exit()

            if commit_info['parent'] == self.current_branch:
                if len(files_to_found) != len(changes):
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

    def write_changes(self, branch_name: str, commit_info: dict, commit_hash: str) -> None:
        """Function to print changes in a new branch"""

        os.mkdir(f'{self.vcs_path}/commits/{branch_name}/')
        os.mkdir(f'{self.vcs_path}/commits/{branch_name}/{commit_hash}')
        json.dump(commit_info, open(f'{self.vcs_path}/commits/{branch_name}/{commit_hash}/commit_info.json', 'w'))

        current_config = json.load(open(f'{self.vcs_path}/config.json', 'r'))
        current_config[branch_name] = commit_hash
        json.dump(current_config, open(f'{self.vcs_path}/config.json', 'w'))
