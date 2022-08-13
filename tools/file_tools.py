"""
Tools to work with file system
Functions list:
    - Get all files from working directory
    - Check is file exists in working directory
    - Get current branch name
    - Check is .vcs directory exists
"""

# Imports
import os
import json


def get_all_files(working_dir: str) -> list:
    """Function to return list with all files from working_dir"""
    output = []
    for root, dirs, files in os.walk(working_dir):
        for file in files:
            output.append(f'{root.replace(working_dir, "")}/{file}')
    return output


def is_exists(working_dir: str, file_name: str) -> bool:
    """Function to check is file exists in working_dir"""
    for element in get_all_files(working_dir):
        if file_name in element:
            return True
    return False


def get_branch_name(working_dir: str) -> str:
    """Function to get current branch name"""
    return open(f'{working_dir}/.vcs/CURRENT_BRANCH').read()


def is_vcs_initialized(working_dir: str) -> bool:
    """Function to check is .vcs dir exists"""
    return os.path.exists(working_dir + '/.vcs/')


def last_commit_hash(working_dir: str) -> str | None:
    """Function to get last commit hash"""
    with open(f'{working_dir}/.vcs/config.json', 'r') as file:
        config_data = json.load(file)
    if get_branch_name(working_dir) not in config_data:
        return None
    return config_data[get_branch_name(working_dir)]
