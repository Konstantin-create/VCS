from tools.file_tools import *


def is_ignored(working_dir: str, ignore_list: list, file_name: str) -> bool:
    """Function is file ignored"""
    for ignore in ignore_list:
        if ignore in file_name.strip():
            return True
    return False


def get_ignore(working_dir: str) -> list | None:
    """Function to parse .ignore file"""
    if is_exists(working_dir, '.ignore'):
        ignore = []
        with open(f'{working_dir}/.ignore', 'r') as file:
            ignore_file_lines = file.readlines()
        for line in ignore_file_lines:
            if line != '' and not line[0] == '#':
                ignore.append(line.strip())
        return ignore
    return None
