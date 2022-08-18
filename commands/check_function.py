"""
File of check command
Functions:
    - Check commits chain(check commit_info hash and commit hash is the same)
    - Check branches
    - Trying to solve troubles
"""
import os
import sys
import json
from colorama import init, Fore
from tools import generate_hash
from tools import get_branch_name, last_commit_hash

# Colorama init
init()


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
            print(Fore.RED + f'Branch {self.current_branch} not found in .vcs/commits')
            sys.exit()

        current_commit = self.last_commit_hash
        gapes = []
        while True:
            commit_info_path = f'{self.vcs_path}/commits/{self.current_branch}/{current_commit}/commit_info.json'
            if not os.path.exists(commit_info_path):
                print(Fore.RED + f'Commit {current_commit} not found')
                sys.exit()

            try:
                commit_info = json.load(open(commit_info_path, 'r'))
            except json.decoder.JSONDecodeError:
                print(Fore.RED + f'Conflicted commit: {current_commit}. The commit info file has been corrupted!')
                sys.exit()
            if current_commit != generate_hash(str(commit_info).encode()):
                print(Fore.RED + f'Conflicted commit: {current_commit}. Commit info were modified!')
                gapes.append(current_commit)
            else:
                print(Fore.GREEN + f'Valid commit: {current_commit}')
            if commit_info['parent'] == self.current_branch:
                break
            current_commit = commit_info['parent']

    def branch_exists(self) -> bool:
        """Function to check is branch exists"""

        return os.path.exists(f'{self.vcs_path}/commits/{self.current_branch}')
