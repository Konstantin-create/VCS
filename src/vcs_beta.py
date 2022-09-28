"""In this file I'm gonna create some skeletons for commands using arg parser"""

import os
import argparse

from commands import *

cwd = os.getcwd()
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(title='subcommands',
                                   description='valid subcommands',
                                   help='description')


def init(args):
    Init(
        cwd,
        base_branch=args.branch or 'main',
        quiet=False or args.quiet
    )


def add(args):
    add = Add(cwd)
    if args.list:
        add.tracked_files_list()
    elif args.clean:
        add.tracked_files_clean()
    else:
        for file in args.file:
            add.add_tracked_file(file, False or args.verbose, False or args.force)


def commit(args):
    print('Commit')
    print(args)


def reset(args):
    print('Reset')
    print(args)


def rollback(args):
    print('Rollback')
    print(args)


def checkout(args):
    print('Checkout')
    print(args)


def branch(args):
    print('Branch')
    print(args)


def merge(args):
    print('Merge')
    print(args)


def ignore(args):
    print('Ignore')
    print(args)


def status(args):
    print('Status')
    print(args)


def check(args):
    print('Check')
    print(args)


# Init parser
init_parser = subparsers.add_parser('init', help='Initial command')
init_parser.add_argument(
    '-q', '--quiet',
    action='store_true',
    dest='quiet',
    help='initialize vcs in quiet mode'
)
init_parser.add_argument(
    '-b', '--branch',
    metavar='quiet', dest='branch',
    help='default branch name'
)
init_parser.set_defaults(func=init)

# Add Parser
add_parser = subparsers.add_parser('add', help='Command to add files in tracked list')
add_parser.add_argument(  # Replace with subparser. Remove flag -f
    '-f', '--filename',
    metavar='filename', nargs='+',
    help='add(use . for add all files) file in a tracked list'
)
add_parser.add_argument(
    '-l', '--list',
    action='store_true',
    dest='list',
    help='print list of tracked files'
)
add_parser.add_argument(
    '-c', '--clean',
    action='store_true',
    dest='clean',
    help='clean list of tracked files'
)
add_parser.add_argument(
    '-v', '--verbose',
    action='store_true',
    dest='verbose',
    help='add files in tracked list in verbose mode'
)
# Error in flag -f. If I change it to -F it works...
add_parser.add_argument(
    '-F', '--force',
    action='store_true',
    dest='force',
    help='add files in tracked list in force mode'
)
add_parser.set_defaults(func=add)

# Commit parser
commit_parser = subparsers.add_parser('commit', help='Command to commit changes')
commit_parser.add_argument(
    '-t', '--text',
    help='create commit with message', required=True
)
commit_parser.add_argument(
    '--HARD',
    action='store_true',
    dest='hard',
    help='commit in hard mode(remove previous commits)'
)
commit_parser.set_defaults(func=commit)

# Reset parser
reset_parser = subparsers.add_parser('reset', help='Command to reset last commit')
reset_parser.add_argument(
    '-v', '--verbose',
    action='store_true',
    dest='verbose',
    help='rollback to last commit in verbose mode'
)
reset_parser.set_defaults(func=reset)

# Rollback parser
rollback_parser = subparsers.add_parser('rollback', help='Command to rollback to last commit')
rollback_parser.add_argument(
    '-v', '--verbose',
    nargs='?', default=True,
    help='rollback to last commit in verbose mode'
)
rollback_parser.set_defaults(func=rollback)

# Checkout parser
checkout_parser = subparsers.add_parser('checkout', help='Switch branches')
checkout_parser.add_argument(
    '-b', '--branch',
    help='switch branch'
)
checkout_parser.add_argument(
    '-n', '--new',
    help='create branch and switch'
)
checkout_parser.set_defaults(func=checkout)

# Branch parser
branch_parser = subparsers.add_parser('branch', help='Command to modify branches')
branch_parser.add_argument(
    '-l', '--list',
    nargs='?', default=True,
    help='command to modify branches'
)
branch_parser.add_argument(
    '-n', '--new',
    help='create new branch'
)
branch_parser.add_argument(
    '-d', '--delete',
    help='remove branch'
)
branch_parser.set_defaults(func=branch)

# Merge parser
merge_parser = subparsers.add_parser('merge', help='Command to merge branches')
merge_parser.add_argument(
    'branch_name',
    help='merge branch_name with current branch in rebase mode'
)
merge_parser.set_defaults(func=merge)

# Ignore parser
ignore_parser = subparsers.add_parser('ignore', help='Command to modify ignore file')
ignore_parser.add_argument(
    '-tl', '--template-list',
    nargs='?', default=True,
    help='print list  of templates'
)
ignore_parser.add_argument(
    '-l', '--list',
    nargs='?', default=True,
    help='get list of ignores'
)
ignore_parser.add_argument(
    '-n', '--new',
    help='create .ignore file with base ignores'
)
ignore_parser.add_argument(
    '-d', '--default',
    help='create .ignore file with base ignores and template'
)
ignore_parser.set_defaults(func=ignore)

# Log parser
log_parser = subparsers.add_parser('log', help='Command to print info about commits')
log_parser.add_argument(
    '-a', '--all',
    nargs='?', default=True,
    help='print all commits'
)

# Status parser
status_parser = subparsers.add_parser('status', help='command to print current vcs status')
status_parser.add_argument(
    ' ',
    nargs='?', default=True,
    help='base command to print status'
)
status_parser.set_defaults(func=status)

# Check parser
check_parser = subparsers.add_parser('check', help='Command to check vcs state')
check_parser.add_argument(
    '-c', '--commits',
    nargs='?', default=True,
    help='command to check vcs state'
)
check_parser.add_argument(
    '-b', '--branches',
    nargs='?', default=True,
    help='check is branches valid'
)
check_parser.set_defaults(func=check)

if __name__ == '__main__':
    args = parser.parse_args()
    if not vars(args):
        parser.print_usage()
    else:
        args.func(args)
