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
import shutil
from colorama import init, Fore
from tools import last_commit_hash, get_branch_name, decode_file

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

    def last_commit(self, verbose: bool = False) -> None:
        """Function to reset last commit"""

        # Check is user want to reset initial commit
        if os.path.exists(f'{self.vcs_path}/commits/{self.branch_name}/{self.last_commit_hash}/commit_info.json'):
            with open(f'{self.vcs_path}/commits/{self.branch_name}/{self.last_commit_hash}/commit_info.json') as file:
                previous_commit = json.load(file)['parent']
        else:
            print(f'{self.vcs_path}/commits/{self.branch_name}/{self.last_commit_hash}/commit_info.json not exists!')
        if previous_commit == self.branch_name:
            print(Fore.RED + 'You cant reset initial commit')
            sys.exit()

        changes = []
        for file in self.tracked_files:
            file_commits = self.check_file_objects(file[list(file.keys())[0]])  # Get file data hashes
            if not len(file_commits):  # Where file object from commit to found
                print(Fore.RED + 'Commit storage error')
                sys.exit()

            if len(file_commits) > 1:
                last_file_data = self.found_last_file_hash(file[list(file.keys())[0]])  # Found file data hashes
                if last_file_data:
                    changes.append(
                        {
                            list(file.keys())[0]: [  # File name
                                file[list(file.keys())[0]],  # File name hash
                                last_file_data  # File last data hash
                            ]
                        }
                    )
                else:
                    print(Fore.RED + 'Commit storage error')
                    sys.exit()
            else:
                changes.append(
                    {
                        list(file.keys())[0]: [  # File name
                            file[list(file.keys())[0]],  # File name hash
                            file_commits[0]  # File last data hash
                        ]
                    }
                )
        print(f'Rollback to commit {previous_commit}')
        print(f'Changes to rewrite: {len(changes)}')
        print()
        if verbose:
            for file in changes:
                print(f'    File name: {list(file.keys())[0]}')
                print(f'    File data hash: {file[list(file.keys())[0]][1]}')
                print()
        print(Fore.GREEN + 'Lucky rollback')
        self.recovery_files(changes)
        self.remove_last_commit()

    def check_file_objects(self, file_hash: str) -> list:
        """Function to get file objects"""

        file_obj_path = f'{self.vcs_path}/objects/{file_hash}'
        if not os.path.exists(file_obj_path):
            return []
        else:
            return [file for file in os.listdir(file_obj_path) if os.path.isfile(os.path.join(file_obj_path, file))]

    def found_last_file_hash(self, filename_hash: str) -> str:
        """Found last file hash function"""

        if os.path.exists(f'{self.vcs_path}/commits/{self.branch_name}/{self.last_commit_hash}/commit_info.json'):
            with open(f'{self.vcs_path}/commits/{self.branch_name}/{self.last_commit_hash}/commit_info.json') as file:
                current_commit = json.load(file)['parent']
        else:
            print(f'{self.vcs_path}/commits/{self.branch_name}/{self.last_commit_hash}/commit_info.json not exists!')
            sys.exit()

        while True:
            if os.path.exists(f'{self.vcs_path}/commits/{self.branch_name}/{current_commit}/commit_info.json'):
                with open(
                        f'{self.vcs_path}/commits/{self.branch_name}/{current_commit}/commit_info.json', 'r'
                ) as file:
                    commit_data = json.load(file)

                for file in commit_data['changes']:
                    if filename_hash in file:
                        return file[filename_hash]

                if commit_data['parent'] == self.branch_name:
                    print(Fore.RED + 'Commit storage error')
                    sys.exit()
                current_commit = commit_data['parent']

    def recovery_files(self, changes: list) -> None:
        """Function to rewrite all files"""
        for file in changes:
            decode_file(
                f'{self.vcs_path}/objects/{file[list(file.keys())[0]][0]}/{file[list(file.keys())[0]][1]}',
                f'{self.working_dir}/{list(file.keys())[0]}'
            )

    def remove_last_commit(self) -> None:
        """Function to remove last commit"""

        if os.path.exists(f'{self.vcs_path}/commits/{self.branch_name}/{self.last_commit_hash}/commit_info.json'):
            with open(f'{self.vcs_path}/commits/{self.branch_name}/{self.last_commit_hash}/commit_info.json',
                      'r') as file:
                previous_commit_hash = json.load(file)['parent']

        # Set new config data
        if os.path.exists(f'{self.vcs_path}/config.json'):
            with open(f'{self.vcs_path}/config.json', 'r') as file:
                config_data = json.load(file)
            config_data[self.branch_name] = previous_commit_hash
            json.dump(config_data, open(f'{self.vcs_path}/config.json', 'w'))
        else:
            print(Fore.RED + '.vcs/config.json is not exists')
            sys.exit()

        # Remove .vcs/commits/<branch_name>/<commit_hash>
        if os.path.exists(f'{self.vcs_path}/commits/{self.branch_name}/{self.last_commit_hash}'):
            shutil.rmtree(f'{self.vcs_path}/commits/{self.branch_name}/{self.last_commit_hash}')
        else:
            print(Fore.RED + f'.vcs/commits/{self.branch_name}/{self.last_commit_hash} not exists')
