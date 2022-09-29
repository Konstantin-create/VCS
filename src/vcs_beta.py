"""In this file I'm gonna create some skeletons for commands using arg parser"""

import os
import argparse

from commands import *

cwd = os.getcwd()
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(title='subcommands',
                                   description='valid subcommands',
                                   help='description')


def init_router(args: argparse.Namespace):
    Init(
        cwd,
        base_branch=args.branch or 'main',
        quiet=bool(args.quiet)
    )


def add_router(args: argparse.Namespace):
    add = Add(cwd)
    if args.list:
        add.tracked_files_list()
    elif args.clean:
        add.tracked_files_clean()
    else:
        for file in args.file:
            add.add_tracked_file(file, bool(args.verbose), bool(args.force))


def commit_router(args: argparse.Namespace):
    commit = Commit(cwd, args.text)
    commit.hard_commit() if args.hard else commit.commit()


def reset_router(args: argparse.Namespace):
    reset = Reset(cwd)
    reset.last_commit(verbose=bool(args.verbose))


def rollback_router(args: argparse.Namespace):
    rollback = Rollback(cwd)
    rollback.rollback(verbose=args.verbose)


def checkout_router(args: argparse.Namespace):
    checkout = CheckOut(cwd)
    checkout.checkout(args.branch, create_new_branch=bool(args.new))


def branch_router(args: argparse.Namespace):
    branch = Branch(cwd)
    if args.list:
        branch.branches_list()
        return
    if args.new:
        branch.create_new(args.new)
        return
    if args.delete:
        branch.remove_branch(args.delete, bool(args.force))


def merge_router(args: argparse.Namespace):
    merge = Merge(cwd)
    merge.merge(args.branch_name)


def ignore_router(args: argparse.Namespace):
    ignore = Ignore(cwd)
    if args.template_list:
        ignore.get_template_list()
        return
    if args.list:
        ignore.get_ignore_list()
        return
    if args.new:
        ignore.create_file(args.template)


def status_router(args: argparse.Namespace):
    status = Status(cwd)
    status.status()


def check_router(args):
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
init_parser.set_defaults(func=init_router)

# Add Parser
add_parser = subparsers.add_parser('add', help='Command to add files in tracked list')
add_parser.add_argument(  # Replace with subparser. Remove flag -f
    '-f', '--filename',
    metavar='filename', nargs='+',
    dest='filename',
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
add_parser.set_defaults(func=add_router)

# Commit parser
commit_parser = subparsers.add_parser('commit', help='Command to commit changes')
commit_parser.add_argument(
    '-t', '--text',
    dest='text',
    help='create commit with message', required=True
)
commit_parser.add_argument(
    '--HARD',
    action='store_true',
    dest='hard',
    help='commit in hard mode(remove previous commits)'
)
commit_parser.set_defaults(func=commit_router)

# Reset parser
reset_parser = subparsers.add_parser('reset', help='Command to reset last commit')
reset_parser.add_argument(
    '-v', '--verbose',
    action='store_true',
    dest='verbose',
    help='rollback to last commit in verbose mode'
)
reset_parser.set_defaults(func=reset_router)

# Rollback parser
rollback_parser = subparsers.add_parser('rollback', help='Command to rollback to last commit')
rollback_parser.add_argument(
    '-v', '--verbose',
    action='store_true',
    dest='verbose',
    help='rollback to last commit in verbose mode'
)
rollback_parser.set_defaults(func=rollback_router)

# Checkout parser
checkout_parser = subparsers.add_parser('checkout',
                                        help='Switch branches')  # todo: rewrite with subparser(remove flags -b and -n)
checkout_parser.add_argument(
    '-b', '--branch',
    dest='branch',
    help='switch branch'
)
checkout_parser.add_argument(
    '-n', '--new',
    dest='new',
    help='create branch and switch'
)
checkout_parser.set_defaults(func=checkout_router)

# Branch parser
branch_parser = subparsers.add_parser('branch', help='Command to modify branches')
branch_parser.add_argument(
    '-l', '--list',
    action='store_true',
    dest='list',
    help='command to modify branches'
)
branch_parser.add_argument(
    '-n', '--new',
    dest='new',
    help='create new branch'
)
branch_parser.add_argument(
    '-d', '--delete',
    dest='delete',
    help='remove branch'
)
branch_parser.add_argument(
    '-f', '--force',
    dest='force',
    action='store_true',
    help='remove branch in a force mode'
)
branch_parser.set_defaults(func=branch_router)

# Merge parser
merge_parser = subparsers.add_parser('merge', help='Command to merge branches')
merge_parser.add_argument(
    'branch_name',
    help='merge branch_name with current branch in rebase mode'
)
merge_parser.set_defaults(func=merge_router)

# Ignore parser
ignore_parser = subparsers.add_parser('ignore', help='Command to modify ignore file')
ignore_parser.add_argument(
    '-tl', '--template-list',
    dest='template_list',
    action='store_true',
    help='print list  of templates'
)
ignore_parser.add_argument(
    '-l', '--list',
    dest='list',
    action='store_true',
    help='get list of ignores'
)
ignore_parser.add_argument(
    '-n', '--new',
    dest='new',
    help='create .ignore file with base ignores'
)
ignore_parser.add_argument(
    '-d', '--default',
    dest='default',
    help='create .ignore file with base ignores and template'
)
ignore_parser.set_defaults(func=ignore_router)

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
status_parser.set_defaults(func=status_router)

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
check_parser.set_defaults(func=check_router)

if __name__ == '__main__':
    args = parser.parse_args()
    if not vars(args):
        parser.print_usage()
    else:
        args.func(args)
