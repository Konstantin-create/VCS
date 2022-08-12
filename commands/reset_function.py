"""
File of reset command
Functions:
    - Reset last commit
    - Reser commit by hash
"""

# Imports
import os
import sys
import json
from colorama import init, Fore
from tools import last_commit_hash, get_branch_name


# Colorama init
init()


# Functions
def get_tracked_files(working_dir) -> None:
    """Function to print list of current tracked files"""
    if os.path.exists(f'{working_dir}/.vcs/tracked_files.json'):
        with open(f'{working_dir}/.vcs/tracked_files.json', 'r', encoding='utf-8') as file:
            if len(file.read()):
                current_tracking = json.load(open(f'{working_dir}/.vcs/tracked_files.json'))
                return current_tracking
    print(Fore.YELLOW + 'No tracking files. Use "vcs add <file_name | -A | .>"')
    sys.exit()


class Reset:
    """Class of reset command"""
    
    def __init__(self, working_dir: str):
        self.working_dir = working_dir
        self.vcs_path = f'{working_dir}/.vcs'
        self.branch_name = get_branch_name(self.working_dir)
        self.last_commit_hash = last_commit_hash(self.working_dir)
        self.tracked_files = get_tracked_files(self.working_dir)


    def last_commit(self) -> None:
        """Function to reset last commit"""
        for file in self.tracked_files:
            file_commits = self.check_file_objects(file[list(file.keys())[0]])
            if not len(file_commits):
                pass
            elif len(file_commits) - 1:
                self.found_last_commit(file[list(file.keys())[0]])
            else:
                pass # todo when 1 commit found


    def check_file_objects(self, file_hash: str) -> list:
        """Function to get file objects"""

        file_obj_path = f'{self.vcs_path}/objects/{file_hash}'
        if not os.path.exists(file_obj_path):
            return []
        else:
            return [file for file in os.listdir(file_obj_path) if os.path.isfile(os.path.join(file_obj_path, file))]

    def found_last_commit(self, file_hash: str) -> str:
        """Function to find last file commit in commit folder"""
        commits_path = f'{self.vcs_path}/commits/{self.branch_name}'

        if os.path.exists(f'{commits_path}/{self.last_commit_hash}/commit_info.json'):
            with open(f'{commits_path}/{self.last_commit_hash}/commit_info.json', 'r') as file:
                commit_data = json.load(file)
            for file in commit_data['changes']:
                if file_hash in file:
                    return file[list(file.keys())[0]]

