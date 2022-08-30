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
from rich import print
from datetime import datetime
from tools import generate_hash, decode_file
from tools import get_branch_name, last_commit_hash, get_tracked_files, get_changes, branch_last_commit


class CheckOut:
    """Function of checkout command"""
    __slots__ = ('working_dir', 'vcs_path', 'current_branch', 'last_commit_hash', 'tracked_files')

    def __init__(self, working_dir: str):
        self.working_dir = working_dir
        self.vcs_path = f'{self.working_dir}/.vcs'
        self.current_branch = get_branch_name(self.working_dir)
        self.last_commit_hash = last_commit_hash(self.working_dir)
        self.tracked_files = get_tracked_files(self.working_dir)

    def checkout(self, branch_name: str = '', create_new_branch: bool = False) -> None:
        """Function to switch branch"""

        if branch_name == self.current_branch:
            print(f'[yellow]Already on {branch_name}[/yellow]')
            sys.exit()
        if not self.is_branch_exists(branch_name) and not create_new_branch:
            print(f'[red]No such branch {branch_name}. To create a new branch use -b flag. '
                  f'More in "vcs checkout -h | --help"[/red]')
            return

        if not self.is_branch_exists(branch_name) and create_new_branch:
            os.mkdir(f'{self.vcs_path}/commits/{branch_name}')
            commit_info = self.create_commit_hash(branch_name)
            commit_hash = generate_hash(str(commit_info).encode())
            os.mkdir(f'{self.vcs_path}/commits/{branch_name}/{commit_hash}')
            json.dump(commit_info, open(f'{self.vcs_path}/commits/{branch_name}/{commit_hash}/commit_info.json', 'w'))
            self.edit_config(branch_name, commit_hash)
        print(f'Switch to branch {branch_name}')
        self.change_current_branch(branch_name)
        changes = get_changes(
            self.working_dir, branch_name, self.tracked_files, branch_last_commit(self.working_dir, branch_name)
        )

        for file in changes:
            filename_hash = list(file.keys())[0]
            for filename in self.tracked_files:
                if filename[list(filename.keys())[0]] == filename_hash:
                    filename = list(filename.keys())[0]
                    decode_file(
                        f'{self.vcs_path}/objects/{filename_hash}/{file[filename_hash]}',
                        f'{self.working_dir}/{filename}'
                    )
                    break

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
        if branch_name not in config_data:
            config_data[branch_name] = branch_last_commit(self.working_dir, branch_name)
        json.dump(config_data, open(f'{self.vcs_path}/config.json', 'w'))

    def edit_config(self, branch_name: str, commit_hash: str):
        """Function to set commit hash in config"""

        current_config = json.load(open(f'{self.vcs_path}/config.json', 'r'))
        current_config[branch_name] = commit_hash
        json.dump(current_config, open(f'{self.vcs_path}/config.json', 'w'))

    def create_commit_hash(self, new_branch_name: str) -> dict:
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
                print('[red]Commit storage error[/red]')
                sys.exit()

            if commit_info['parent'] == self.current_branch:
                if len(files_to_found) != len(changes):
                    print('[red]Commit storage error[/red]')
                    print(f'[red]Elements {files_to_found} not found[/red]')
                    sys.exit()
                break
            current_commit = commit_info['parent']

        return {
            'message': f'Merged from {self.current_branch}',
            'changes': changes,
            'time_stamp': str(datetime.utcnow()),
            'parent': new_branch_name
        }
