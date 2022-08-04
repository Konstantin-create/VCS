import os
import json
import shutil


class Init:
    """Class to init vcs working dir"""
    def __init__(self, run_path, base_branch='master'):
        self.run_path = run_path
        self.create_vcs_dir()
        self.create_config(str(base_branch))

        print('\nVCS initialized successfully')
        

    def create_vcs_dir(self) -> None:
        """Function to create .vcs dir in working dir"""
        if os.path.exists(f'{self.run_path}/.vcs'):
            print('In this directory, the version control system is already initialized')
            command = input('Recreate .vcs folder? yes/No: ').strip().lower()
            if 'n' in command:
                return
            else:
                shutil.rmtree(self.run_path + '/.vcs')

        os.mkdir(self.run_path + '/.vcs')
        os.mkdir(self.run_path + '/.vcs/refs')
        os.mkdir(self.run_path + '/.vcs/refs/heads')

    def create_config(self, main_branch: str):
        merge_path = self.run_path + '/.vcs/refs/heads/' + main_branch
        print(merge_path)
        os.mkdir(merge_path)
        config_data = {main_branch: {'merge': merge_path}}
        with open(self.run_path + '/.vcs/config.json', 'w') as file:
            json.dump(config_data, file, indent=4)
            
