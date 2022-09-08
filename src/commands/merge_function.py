"""
File of merge function
Functions:
    - Get state from branch and create merge commit in current branch and write this in file
"""

# Imports
import os
import sys
import json
from rich import print
from datetime import datetime
from tools import generate_hash, get_changes, decode_file
from tools import last_commit_hash, get_branch_name, get_tracked_files, branch_last_commit


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

        # Check is tracked files are not empty
        if not len(self.tracked_files):
            print('[yellow]No tracked files were found. Try \'vcs add -A\'[/yellow]')
            sys.exit()
        # Check is branch name not current branch
        if branch_name == self.current_branch:
            print('[red]You cant merge current branch with the same branch[/red]')
            sys.exit()

        # Check is branches exists
        if not self.is_branch_exists(branch_name):
            print(f'Branch {branch_name} is not found')
            sys.exit()
        if not self.is_branch_exists(self.current_branch):
            print(f'Branch {branch_name} is not exists')
            sys.exit()

        commit_info = self.create_commit_info(branch_name)
        commit_hash = generate_hash(str(commit_info).encode())
        os.mkdir(f'{self.vcs_path}/commits/{self.current_branch}/{commit_hash}')
        json.dump(commit_info,
                  open(f'{self.vcs_path}/commits/{self.current_branch}/{commit_hash}/commit_info.json', 'w'))
        for file_to_save in commit_info['changes']:
            for tracked_file in self.tracked_files:
                if list(file_to_save.keys())[0] == tracked_file[list(tracked_file.keys())[0]]:
                    os.remove(f'{self.working_dir}/{list(tracked_file.keys())[0]}')
                    decode_file(
                        f'{self.vcs_path}/objects/'
                        f'{list(file_to_save.keys())[0]}/{file_to_save[list(file_to_save.keys())[0]]}',
                        f'{self.working_dir}/{list(tracked_file.keys())[0]}')
        print(f'[green]Successfully merged from {branch_name}. Merge commit: {commit_hash}[/green]')

    def create_commit_info(self, new_branch_name: str) -> dict:
        """Function to create commit info"""

        return {
            'message': f'Merged from {new_branch_name}',
            'changes': get_changes(self.working_dir, new_branch_name, self.tracked_files,
                                   branch_last_commit(self.working_dir, new_branch_name)),
            'time_stamp': str(datetime.utcnow()),
            'parent': self.last_commit_hash
        }

    def is_branch_exists(self, branch_name: str) -> bool:
        """Function to check is branch exists"""

        return os.path.exists(f'{self.vcs_path}/commits/{branch_name}')
