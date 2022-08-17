"""
Tools for branch functions file
Functions:
    - Get list of branches
    - Get list of changes
"""

# Imports
import os
import sys
import json
from colorama import init, Fore

# Colorama init
init()


def get_branches(working_dir: str) -> list:
    """Function to get list of branches"""

    return list(json.load(open(f'{working_dir}/.vcs/config.json', 'r')).keys())


def get_changes(working_dir: str, branch_name: str, tracked_files: list, last_commit_hash) -> list:
    """Function to get list of changes"""

    vcs_path = f'{working_dir}/.vcs/'

    files_to_found = []  # List of files which last version we find in commit tree
    changes = []  # List of last version hashes like [{'<filename_hash>': '<file_data_hash>'}, ...]
    for file in tracked_files:
        files_to_found.append(file[list(file.keys())[0]])
    current_commit = last_commit_hash

    while True:
        commit_info_path = f'{vcs_path}/commits/{branch_name}/{current_commit}/commit_info.json'
        if os.path.exists(commit_info_path):
            commit_info = json.load(open(commit_info_path, 'r'))

            for filename in files_to_found:
                for bin_file in commit_info['changes']:
                    if filename in bin_file:
                        changes.append({filename: bin_file[filename]})
                        files_to_found.remove(filename)
        else:
            print(Fore.RED + 'Commit storage error')
            sys.exit()

        if commit_info['parent'] == branch_name:
            # if len(files_to_found) != len(changes):
            #     print(Fore.RED + 'Commit storage error')
            #     print(Fore.RED + f'Elements {files_to_found} not found')
            #     sys.exit()
            break
        current_commit = commit_info['parent']
    return changes


def branch_last_commit(working_dir: str, branch_name: str) -> str:
    config = json.load(open(f'{working_dir}/.vcs/config.json', 'r'))
    if branch_name not in config:
        return ''
    return config[branch_name]
