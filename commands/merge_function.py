"""
File of merge function
Functions:
    - Get state from branch and create merge commit in current branch and write this in file
"""

# Imports
import os
import sys
from colorama import init, Fore
from tools import last_commit_hash, get_branch_name, get_tracked_files

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

    def merge(self, branch_name: str):
        """Function to merge branches"""

        pass
