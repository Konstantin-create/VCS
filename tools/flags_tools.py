"""
Tool of flags
Contains flags for:
    - Add command flags
    - Commit command flags
    - Checkout command flags
    - Ignore command flags
"""

add_flags = ['-l', '--list', '-h', '--help', '-c', '--clean', '-v', '--verbose', '-f', '--force']
commit_flags = ['-t', '--hard', '--HARD', '-h', '--help']
checkout_flags = ['-b', '--branch', '-h', '--help']
ignore_flags = ['-n', '--new', '-t', '--template', '-tl', '--template-list']
