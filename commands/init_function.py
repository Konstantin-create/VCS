import os
import json
import shutil
from colorama import init, Fore

# Colorama init
init(autoreset=True)


class Init:
    """Class to init vcs working dir"""

    def __init__(self, run_path, base_branch='master'):
        self.run_path = run_path
        self.branch_name = base_branch
        self.create_vcs_dir()
        print(Fore.GREEN + '\nVCS initialized successfully')

    def create_vcs_dir(self) -> None:
        """Function to create .vcs dir in working dir"""
        if os.path.exists(f'{self.run_path}/.vcs'):
            print(Fore.YELLOW + 'In this directory, the version control system is already initialized')
            command = input('Recreate .vcs folder? yes/No: ').strip().lower()
            if 'n' in command:
                return
            else:
                shutil.rmtree(self.run_path + '/.vcs')

        self.create_folders()
        self.create_config(str(self.branch_name))

    def create_folders(self):
        """Function to create base folders for .vcs init"""
        os.mkdir(self.run_path + '/.vcs')
        os.mkdir(self.run_path + '/.vcs/commits')
        os.mkdir(self.run_path + '/.vcs/commits/' + self.branch_name)
        os.mkdir(self.run_path + '/.vcs/objects')
        os.mkdir(self.run_path + '/.vcs/refs')
        os.mkdir(self.run_path + '/.vcs/refs/heads')

    def create_config(self, main_branch: str):
        merge_path = self.run_path + '/.vcs/refs/heads/' + main_branch + '.txt'
        with open(merge_path, 'w') as file:
            file.write('')
        print(Fore.YELLOW + f'Set main branch as {self.branch_name}')
        config_data = {main_branch: {'merge': merge_path}}
        with open(self.run_path + '/.vcs/config.json', 'w') as file:
            json.dump(config_data, file, indent=4)
