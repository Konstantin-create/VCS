"""
Tools for print help text in commands
Functions:
    - Index command  help text
    - Add command help text
    - Commit command help text
    - Ignore command help text
"""

# Vars with help text

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

ignore_text = """
vcs ignore -n | --new - Create .ignore file with base ignores
vcs ignore -h | --help - This help
"""

# Print help functions
def init_help():
    print(init_text)


def add_help():
    print(add_text)


def commit_help():
    print(commit_text)

def ignore_help():
    print(ignore_text)

