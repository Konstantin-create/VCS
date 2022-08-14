"""
File of status function
Functions:
    - Print current branch name
    - Print changes to commit
"""

# Imports
import os
from colorama import init, Fore
from tools import generate_hash
from tools import get_branch_name, last_commit_hash, get_tracked_files

# Colorama init
init(autoreset=True)


class Status:
    """Class of status command"""

    def __init__(self, working_dir: str):
        self.working_dir = working_dir
        self.vcs_path = f'{self.working_dir}/.vcs'
        self.branch_name = get_branch_name(self.working_dir)
        self.last_commit_hash = last_commit_hash(self.working_dir)
        self.tracked_files = get_tracked_files(self.working_dir)

    def status(self):
        """Function to print vcs status"""
        print(f'On branch {Fore.YELLOW + self.branch_name}')
        print()
        self.get_changes()

    def get_changes(self) -> list:
        """Function to get changes"""
        deleted = []
        modified = []
        for tracked_file in self.tracked_files:
            filename = list(tracked_file.keys())[0]
            if not os.path.exists(f'{self.working_dir}/{filename}'):
                deleted.append(filename)
            else:
                with open(f'{self.working_dir}/{filename}', 'rb') as file:
                    file_data = generate_hash(file.read())
                if not os.path.exists(f'{self.vcs_path}/objects/{tracked_file[filename]}/{file_data}'):
                    modified.append(filename)

        print(
            {'modified': modified, 'deleted': deleted}
        )
