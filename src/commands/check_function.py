"""
File of check command
Functions:
    - Check commits chain(check commit_info hash and commit hash is the same)
    - Check branches
    - Trying to solve troubles
"""
import os
import shutil
import sys
import json
from rich import print
from tools import generate_hash
from tools import get_branch_name, last_commit_hash


class Checker:
    """Check command class"""
    __slots__ = ('working_dir', 'vcs_path', 'last_commit_hash', 'current_branch')

    def __init__(self, working_dir: str):
        self.working_dir = working_dir
        self.vcs_path = f'{working_dir}/.vcs'
        self.last_commit_hash = last_commit_hash(self.working_dir)
        self.current_branch = get_branch_name(self.working_dir)

    def check_commits_chain(self):
        """Function to check is commit_info hash is the similar with commit_hash"""

        if not self.branch_exists():
            print(f'[red]Branch {self.current_branch} not found in .vcs/commits[/red]')
            sys.exit()

        current_commit = self.last_commit_hash
        gapes = []
        while True:
            commit_info_path = f'{self.vcs_path}/commits/{self.current_branch}/{current_commit}/commit_info.json'
            if not os.path.exists(commit_info_path):
                print(f'[red]Commit {current_commit} not found[/red]')
                sys.exit()

            try:
                commit_info = json.load(open(commit_info_path, 'r'))
            except json.decoder.JSONDecodeError:
                print(f'[red]Conflicted commit: {current_commit}. The commit info file has been corrupted![/red]')
                sys.exit()
            if current_commit != generate_hash(str(commit_info).encode()):
                print(f'[red]Conflicted commit: {current_commit}. Commit info were modified![/red]')
                gapes.append(current_commit)
            else:
                print(f'[green]Valid commit: {current_commit}[/green]')
            if commit_info['parent'] == self.current_branch:
                break
            current_commit = commit_info['parent']

    def check_branches(self):
        """Function to check branches"""

        branches = os.listdir(f'{self.vcs_path}/commits')
        config_items_delete = []  # List of commit items to delete

        if not os.path.exists(f'{self.vcs_path}/config.json'):
            print('[red]Config file not found. Try to reinitialize vcs[/red]')
            sys.exit()

        try:
            config = json.load(open(f'{self.vcs_path}/config.json', 'r'))
        except json.decoder.JSONDecodeError:
            print('[red]The config file has been corrupted[/red]')
            sys.exit()

        for file_name in config:
            if file_name in branches:
                print(f'[green]Valid branch: {file_name}[/green]')
                branches.remove(file_name)
            else:
                print()
                command = input(
                    f'[red]Critical:[/red] Branch {file_name} not found. Remove from config(yes/No): '
                )
                if 'y' in command:
                    config_items_delete = {file_name: config[file_name]}
        print()
        if len(config_items_delete):  # Check config file by branches which are not in commits/
            for item in config_items_delete:
                del config[item]
            json.dump(config, open(f'{self.vcs_path}/config.json', 'w'))

        print()

        if len(branches) >= 1:  # Check branch list from commits/ are exists in config.json
            for branch_name in branches:
                command = input(
                    f'[yellow]Warning:[/yellow] '
                    f'Find branch \'{branch_name}\' in commits folder. Select action:\n  1 - Remove\n  2 - Ignore\n~ '
                )
                if command.isdigit() and int(command) == 1:
                    shutil.rmtree(f'{self.vcs_path}/commits/{branch_name}')
                    print('[green]Successfully removed from .vcs/commits/[/green]')
                    print()

        tmp_config = config
        for branch in config:  # Find branches in config without pointer on last commit
            if config[branch] == '':
                print(f'[red]Critical:[/red] Branch \'{branch}\' have no pointer to last hash!')
                command = input('Choose action:\n  1 - Remove this branch name from config and commits(if exists)\n  '
                                '2 - Set pointer to last commit\n~ ')
                if command.isdigit() and int(command) == 1:
                    del tmp_config[branch]
                    json.dump(tmp_config, open(f'{self.vcs_path}/config.json', 'w'))
                elif command.isdigit() and int(command) == 2:
                    while True:
                        pointer = input('Enter commit hash: ')
                        if os.path.exists(f'{self.vcs_path}/commits/{branch}/{pointer}'):
                            config[branch] = pointer
                            json.dump(config, open(f'{self.vcs_path}/config.json', 'w'))
                            break
                        print(f'[red]Commit {pointer} not found in branch {branch}[/red]')
        # todo: check commit by hash is exists

    def branch_exists(self) -> bool:
        """Function to check is branch exists"""

        return os.path.exists(f'{self.vcs_path}/commits/{self.current_branch}')
