import os


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

