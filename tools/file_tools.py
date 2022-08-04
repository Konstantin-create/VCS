import os

def get_all_files(working_dir: str) -> list:
    """Function to return list with all files from working_dir"""
    output = []
    for root, dirs, files in os.walk(working_dir):
        for file in files:
            output.append(f'{root.replace(working_dir)}/{file}')
    return output
