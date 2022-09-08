"""
File of init command.
Functions:
    - Create .vcs/ tree in working dir
    - Create configs
        - Set up current branch name
        - Create list of branch names
"""

# Imports
import os
import json
import shutil
from rich import print


class Init:
    """Class to init vcs working tree"""
    __slots__ = ('run_path', 'branch_name', 'quiet')

    def __init__(self, run_path: str, base_branch: str = 'master', quiet: bool = False):
        self.run_path = run_path
        self.branch_name = base_branch
        self.quiet = quiet
        self.create_vcs_dir()
        if not quiet:
            print('[green]\nVCS initialized successfully[/green]')

    def create_vcs_dir(self) -> None:
        """Function to create .vcs dir in working dir"""

        if os.path.exists(f'{self.run_path}/.vcs'):
            print('[yellow]In this directory, the version control system is already initialized[/yellow]')
            command = input('Recreate .vcs folder? yes/No: ').strip().lower()
            if 'n' in command:
                return
            else:
                shutil.rmtree(self.run_path + '/.vcs')

        self.create_folders()
        self.create_config(str(self.branch_name))

    def create_folders(self) -> None:
        """Function to create base folders for .vcs init. Create .vcs/ working tree"""

        os.mkdir(self.run_path + '/.vcs')
        os.mkdir(self.run_path + '/.vcs/commits')
        os.mkdir(self.run_path + '/.vcs/commits/' + self.branch_name)
        os.mkdir(self.run_path + '/.vcs/objects')

    def create_config(self, main_branch: str) -> None:
        """Function to create config files in root of .vcs/.
            Where im going to save current branch and list of branch names"""

        if not self.quiet:
            print(f'[yellow]Set main branch as {self.branch_name}[/yellow]')
        config_data = {main_branch: self.branch_name}
        with open(self.run_path + '/.vcs/config.json', 'w') as file:
            json.dump(config_data, file, indent=4)

        with open(f'{self.run_path}/.vcs/CURRENT_BRANCH', 'w') as file:
            file.write(self.branch_name)
