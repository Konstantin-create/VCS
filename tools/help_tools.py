"""
Tools for print help text in commands
Functions:
    - Index command  help text
    - Add command help text
    - Commit command help text
    - Ignore command help text
"""

# Vars with help text

vcs_text = """
vcs init - Initial command
vcs add - Command to add files in tracked list
vcs commit - Command to commit changes
vcs reset - Command to rollback to last commit
vcs ignore - Command to modify ignore file
vcs -h | --help - This help
"""

init_text = """
vcs init
    -b "<branch name>" - Create first branch with custom name
    -q | --quiet - Quiet mode. Only errors and warning
    -h | --help- This help
"""

add_text = """
vcs add <file_name> | . | -A
    . = -A - Add all files in current directory to tracked files list
vcs add
    -l - Print all tracked files list
    -c | --clean - Clear tracked files list
    -v | --verbose - Be verbose
    -f | --force - Disregard .ignore file
    -h | --help - This help
"""

commit_text = """
vcs commit -t "<Your commit text>" - Create commit with text
vcs commit -t "<Your commit text>" --hard - Create commit, and remove all previous commits
vcs commit -h | --help - This help
"""

reset_text = """
vcs reset - Reset to last commit
vcs reset -v | --verbose - Reset to last commit in verbose mode
vcs reset -h | --help
"""

ignore_text = """
vcs ignore 
    -n | --new - Create .ignore file with base ignores
    -t | --template - Create .ignore file with base ignores and template
vcs ignore -tl | --template-list - Print list  of templates
vcs ignore -l | --list - Get list of ignores
vcs ignore -h | --help - This help
"""

log_text = """
vcs log - Print last commit log
vcs log -a | --all - Print all commits
"""


# Print help functions
def vcs_help():
    print(vcs_text)


def init_help():
    print(init_text)


def add_help():
    print(add_text)


def commit_help():
    print(commit_text)


def reset_help():
    print(reset_text)


def ignore_help():
    print(ignore_text)


def log_help():
    print(log_text)
