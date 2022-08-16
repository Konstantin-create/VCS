"""
Tools for branch functions file
Functions:
    - Get list of branches
"""

# Imports
import json


def get_branches(working_dir: str) -> list:
    """Function to get list of branches"""

    return list(json.load(open(f'{working_dir}/.vcs/config.json', 'r')).keys())
