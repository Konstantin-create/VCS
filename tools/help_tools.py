"""
Tools for print help text in commands
Functions:
    - Index command  help text
    - Add command help text
    - Commit command help text
"""

# Vars with help text

init_text = """
vcs init
    -b "<branch name>" - Create first branch with custom name
"""

add_text = """
vcs add <file_name> | . | -A
    . = -A - Add all files in current directory to tracked files list
vcs add
    -l - Print all tracked files list
"""

commit_text = """
vcs commit -t "<You'r commit text>" - Create commit with text
"""

# Print help functions
def init_help():
    print(init_text)


def add_help():
    print(add_text)


def commit_help():
    print(commit_text)
