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
from rich import print
from datetime import datetime
from tools import generate_hash
from tools import get_branch_name, get_branches
from tools import last_commit_hash, get_tracked_files, get_changes


class Branch:
    """Class to manage branches"""
    __slots__ = ('working_dir', 'vcs_path', 'current_branch', 'branches', 'last_commit_hash', 'tracked_files')

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
            print(f'[green]Branch {branch_name} has been created')
            print(f'{len(commit_info["changes"])} files were inherited[/green]')
        else:
            print(f'[red]Branch {branch_name} is already exists[/red]')
            sys.exit()

    def branches_list(self):
        """Function to print list of branches"""

        print('Branches:')
        print('  ' + '\n  '.join(self.branches))
        print()
        print(f'Total {len(self.branches)} branches')

    def remove_branch(self, branch_name: str, force: bool) -> None:
        """Function to remove branch"""

        if len(branch_name) <= 1:
            print('[yellow]You can\'t remove the last branch[/yellow]')
            sys.exit()
        if self.current_branch == branch_name:
            print('[yellow]You can\'t delete the branch you are currently on[/yellow]')
            sys.exit()
        if not self.is_branch_exists(branch_name):
            print(f'[red]Branch {branch_name} not found[/red]')
            sys.exit()

        if force:  # Force mode removing
            self.remove_branch_force(branch_name)
            return
        self.remove_branch_default(branch_name)

    def remove_branch_force(self, branch_name: str) -> None:
        """Function to remove branch in a force mode"""

        print(f'[yellow]Deleting {branch_name} in force mode[/yellow]')
        shutil.rmtree(f'{self.vcs_path}/commits/{branch_name}')
        current_config = json.load(open(f'{self.vcs_path}/config.json', 'r'))
        if branch_name in current_config:
            current_config.pop(branch_name)
            json.dump(current_config, open(f'{self.vcs_path}/config.json', 'w'))
        print(f'Branch {branch_name} was successfully deleted')

    def remove_branch_default(self, branch_name: str) -> None:
        """Function to remove branch in default mode"""

        config = json.load(open(f'{self.vcs_path}/config.json', 'r'))
        if branch_name not in config:
            print('[red]Commit storage error[/red]')
            sys.exit()

        master_changes = get_changes(self.working_dir, self.current_branch, self.tracked_files, self.last_commit_hash)
        current_changes = get_changes(self.working_dir, branch_name, self.tracked_files, config[branch_name])
        difference = []

        if not (len(master_changes) == len(current_changes) == len(self.tracked_files)):
            print('[red]Commit storage error[/red]')
            sys.exit()

        for i in range(len(self.tracked_files)):
            master_file = master_changes[i]
            current_file = current_changes[i]

            if master_file[list(master_file.keys())[0]] != current_file[list(current_file.keys())[0]]:
                difference.append(current_file)

        print(difference)

    def is_branch_exists(self, branch_name: str) -> bool:
        """Function check is branch exists"""

        return os.path.exists(f'{self.vcs_path}/commits/{branch_name}')

    def create_commit_info(self, new_branch_name: str) -> dict:
        """Function to create first commit in a new branch"""

        changes = get_changes(self.working_dir, self.current_branch, self.tracked_files, self.last_commit_hash)

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
