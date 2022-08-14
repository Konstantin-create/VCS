"""
File of commit function
Functions:
    - Create commit
        - Create objects from tracked files list
        - Create commit tree
        - Save last commit hash
"""

# Imports
from __future__ import annotations

import os
import sys
import json
import shutil
from datetime import datetime
from colorama import init, Fore
from tools import generate_hash, pretty_hash
from tools import get_branch_name, is_vcs_initialized, last_commit_hash
from tools import encode_file

# Colorama init
init(autoreset=True)


class Commit:
    """Commit class"""
    __slots__ = ('working_dir', 'vcs_path', 'message', 'last_commit', 'branch_name')

    def __init__(self, working_dir: str, message: str):
        self.working_dir = working_dir
        self.vcs_path = working_dir + '/.vcs'
        self.message = message
        self.last_commit = last_commit_hash(self.working_dir)
        self.branch_name = get_branch_name(self.working_dir)

    def commit(self) -> None:
        """Commit function"""

        if self.last_commit != '':
            self.initial_commit()
            return
        self.child_commit()

    def initial_commit(self, hard_commit=False):
        """Initial commit function"""

        created_objects = self.get_changes()
        if not len(created_objects):
            sys.exit()
        commit_info = self.create_commit_info(created_objects)
        commit_hash = generate_hash(str(commit_info).encode())
        self.create_commit_dir(commit_hash, commit_info)

        with open(f'{self.vcs_path}/config.json', 'r') as file:
            config_data = json.load(file)
        config_data[self.branch_name] = commit_hash
        json.dump(config_data, open(f'{self.vcs_path}/config.json', 'w'))

        if hard_commit:
            print(f'[{self.branch_name} {Fore.RED + pretty_hash(commit_hash) + Fore.WHITE}] {self.message}')
        else:
            print(f'[{self.branch_name} {Fore.GREEN + pretty_hash(commit_hash) + Fore.WHITE}] {self.message}')
        print(f' {len(created_objects)} object have been created')

    def child_commit(self):
        """Child commit function"""

        created_objects = self.get_changes()
        if not len(created_objects):
            sys.exit()
        commit_info = self.create_commit_info(created_objects)
        commit_hash = generate_hash(str(commit_info).encode())

        with open(f'{self.vcs_path}/config.json', 'r') as file:
            config_data = json.load(file)
        config_data[self.branch_name] = commit_hash
        json.dump(config_data, open(f'{self.vcs_path}/config.json', 'w'))

        print(f'[{self.branch_name} {Fore.YELLOW + pretty_hash(commit_hash) + Fore.WHITE}] {self.message}')
        print(f' {len(created_objects)} objects have been created')

    def hard_commit(self):
        """Hard commit function(remove previous changes)"""

        if is_vcs_initialized(self.working_dir):
            if os.path.exists(f'{self.vcs_path}/commits/{self.branch_name}'):
                shutil.rmtree(f'{self.vcs_path}/commits/{self.branch_name}')
            if os.path.exists(f'{self.vcs_path}/objects/'):
                shutil.rmtree(f'{self.vcs_path}/objects/')
            os.mkdir(f'{self.vcs_path}/commits/{self.branch_name}')
            os.mkdir(f'{self.vcs_path}/objects')
            self.initial_commit(hard_commit=True)

    # Global functions block
    # Get block
    def get_tracked_files(self) -> list:
        """Function to get list of tracked files"""

        if not os.path.exists(self.vcs_path + '/tracked_files.json'):
            print(Fore.RED + 'No tracked files found try "vcs add <file_name> | -A | ."')
            sys.exit()
        return json.load(open(self.vcs_path + '/tracked_files.json'))

    def remove_tracked_file(self, filename: str) -> None:
        """Function to remove file from tracked list"""

        current_tracked = self.get_tracked_files()
        for file in current_tracked:
            if filename in file:
                current_tracked.remove(file)
        json.dump(current_tracked, open(self.vcs_path + '/tracked_files.json', 'w'))

    def get_changes(self) -> list:
        """Function to get path to changed files"""

        if not os.path.exists(self.vcs_path + '/objects'):
            print(Fore.RED + '.vcs/objects directory not found. Try "vcs init"')
            sys.exit()

        created_objects = []
        deleted_objects = []
        tracked_files = self.get_tracked_files()
        for file in tracked_files:
            for key in file:
                if not os.path.exists(f'{self.vcs_path}/objects/{file[key]}'):
                    os.mkdir(f'{self.vcs_path}/objects/{file[key]}')
                if os.path.exists(f'{self.working_dir}/{key}'):
                    file_hash = generate_hash(open(f'{self.working_dir}/{key}', 'rb').read())

                    if not os.path.exists(f'{self.vcs_path}/objects/{file[key]}/{file_hash}'):
                        encode_file(self.working_dir + key, f'{self.vcs_path}/objects/{file[key]}/{file_hash}')
                        created_objects.append({file[key]: file_hash})
                else:
                    self.remove_tracked_file(key)
                    deleted_objects.append(key)
        if not deleted_objects:
            if not len(created_objects):
                print(Fore.YELLOW + 'Repo is already up to date')
        else:
            print('Deleted objects:')
            print('  ' + '  '.join(deleted_objects))
        return created_objects

    # Create block
    def create_commit_dir(self, commit_hash, commit_info):
        """Create commit dir and commit_info file"""

        if os.path.exists(f'{self.vcs_path}/commits/{self.branch_name}/{commit_hash}'):
            print(Fore.RED + 'Repo is already up to date')
            sys.exit()
        os.mkdir(f'{self.vcs_path}/commits/{self.branch_name}/{commit_hash}')
        with open(f'{self.vcs_path}/commits/{self.branch_name}/{commit_hash}/commit_info.json', 'w') as file:
            json.dump(commit_info, file, indent=4)

    def create_commit_info(self, changes: list) -> dict:
        """Function to generate commit info"""

        return {
            'message': self.message,
            'changes': changes,
            'time_stamp': str(datetime.utcnow()),
            'parent': self.last_commit
        }
