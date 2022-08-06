import os
import sys
import json
from tools import generate_hash
from tools import encode_file, decode_file
from colorama import init, Fore

# Colorama init
init(autoreset=True)


class Commit:
    def __init__(self, working_dir: str):
        self.working_dir = working_dir
        self.vcs_path = working_dir + '/.vcs'

    def commit(self, message: str) -> None:
        """Commit function"""
        last_commit = self.get_last_commit()
        if not last_commit:
            created_objects = self.get_changes()
            if not len(created_objects):
                sys.exit()



    def get_last_commit(self) -> str | None:
        """Function to get last commit hash"""
        if os.path.exists(self.vcs_path + '/LAST_COMMIT'):
            return open(self.vcs_path + '/LAST_COMMIT').read()
        return None

    def get_tracked_files(self) -> list:
        """Function to get list of tracked files"""
        if not os.path.exists(self.vcs_path + '/tracked_files.json'):
            print(Fore.RED + 'No tracked files found try "vcs add <file_name> | -A | ."')
            sys.exit()
        return json.load(open(self.vcs_path + '/tracked_files.json'))

    def get_changes(self) -> list:
        """Function to get path to changed files"""
        if not os.path.exists(self.vcs_path + '/objects'):
            print(Fore.RED + '.vcs/objects directory not found. Try "vcs init"')
            sys.exit()

        created_objects = []
        tracked_files = self.get_tracked_files()
        for file in tracked_files:
            for key in file:
                if not os.path.exists(f'{self.vcs_path}/objects/{file[key]}'):
                    os.mkdir(f'{self.vcs_path}/objects/{file[key]}')
                file_hash = generate_hash(open(f'{self.working_dir}/{key}', 'rb').read())
                if not os.path.exists(f'{self.vcs_path}/objects/{file[key]}/{file_hash}'):
                    encode_file(self.working_dir + key, f'{self.vcs_path}/objects/{file[key]}/{file_hash}')
                    created_objects.append({file[key]: file_hash})
        if not len(created_objects):
            print(Fore.YELLOW + 'Repo is already up to date')
        else:
            print(f'Created objects: {len(created_objects)}')
        return created_objects

    def create_commit_info(self, changes: list) -> dict:
        """Function to genereate commit info"""
        pass

