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
    __slots__ = 'working_dir'

    def __init__(self, working_dir: str):
        self.working_dir = working_dir

    def get_commit_info(self, commit_hash: str = '') -> None:
        """Function to get commit info by hash or get last commit info"""

        if commit_hash == '':
            if not last_commit_hash(self.working_dir):
                print(Fore.RED + 'You have no commits in this dir')
                return
            if os.path.exists(
                    f'{self.working_dir}/.vcs/commits/'
                    f'{get_branch_name(self.working_dir)}/{last_commit_hash(self.working_dir)}/commit_info.json'):
                with open(
                        f'{self.working_dir}/.vcs/commits/'
                        f'{get_branch_name(self.working_dir)}/{last_commit_hash(self.working_dir)}/commit_info.json',
                        'r') as file:
                    commit_info = json.load(file)
                print(f'Commit: {last_commit_hash(self.working_dir)}')
                print(f'Message: {commit_info["message"]}')
                print(f'Time stamp: {commit_info["time_stamp"]}')
                print(f'Parent: {commit_info["parent"]}')
                print()
        else:
            if os.path.exists(
                    f'{self.working_dir}/.vcs/commits/{get_branch_name(self.working_dir)}/'
                    f'{commit_hash}/commit_info.json'):
                with open(
                        f'{self.working_dir}/.vcs/commits/{get_branch_name(self.working_dir)}/'
                        f'{commit_hash}/commit_info.json') as file:
                    commit_info = json.load(file)
                print(f'Commit: {commit_hash}')
                print(f'Message: {commit_info["message"]}')
                print(f'Time stamp: {commit_info["time_stamp"]}')
                print(f'Parent: {commit_info["parent"]}')
                print()
            else:
                print(Fore.RED + f'Commit {commit_hash} not found!')

    def get_all_commits(self, verbose: bool) -> None:
        """Function to print all of commits"""

        if not last_commit_hash(self.working_dir):
            print(Fore.RED + 'You have no commits in this dir')
            return
        commits_path = f'{self.working_dir}/.vcs/commits/{get_branch_name(self.working_dir)}/'
        if os.path.exists(f'{commits_path}/{last_commit_hash(self.working_dir)}/commit_info.json'):
            with open(f'{commits_path}/{last_commit_hash(self.working_dir)}/commit_info.json') as file:
                last_commit = json.load(file)

            counter = 1
            print()
            print(last_commit_hash(self.working_dir))

            if last_commit['parent'] != get_branch_name(self.working_dir):
                while True:
                    if os.path.exists(f'{commits_path}/{last_commit["parent"]}/commit_info.json'):
                        previous_commit = last_commit['parent']
                        with open(f'{commits_path}/{last_commit["parent"]}/commit_info.json') as file:
                            last_commit = json.load(file)
                        counter += 1
                        if last_commit['parent'] == get_branch_name(self.working_dir):
                            if verbose:
                                if os.path.exists(
                                        f'{self.working_dir}/.vcs/commits/{get_branch_name(self.working_dir)}/'
                                        f'{previous_commit}/commit_info.json'):
                                    with open(
                                            f'{self.working_dir}/.vcs/commits/{get_branch_name(self.working_dir)}/'
                                            f'{previous_commit}/commit_info.json') as file:
                                        commit_info = json.load(file)
                                    print(f'Commit: {Fore.YELLOW + previous_commit + Fore.WHITE} - Initial commit')
                                    print(f'Message: {commit_info["message"]}')
                                    print(f'Time stamp: {commit_info["time_stamp"]}')
                                    print('Parent: Null')
                                else:
                                    print(Fore.RED + f'Commit {previous_commit} not found!')
                                break
                            print(Fore.YELLOW + previous_commit + ' - Initial commit')
                            break
                        if verbose:
                            self.get_commit_info(previous_commit)
                        else:
                            print(previous_commit)

            print()
            print(f'Total {counter} commits found')
        else:
            print(Fore.RED + 'Commit storage error try to use help on https://github.com/Konstantin-create/VCS/')
