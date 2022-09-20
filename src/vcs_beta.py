"""In this file I'm gonna create some skeletons for commands using arg parser"""

import argparse

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(title='subcommands',
                                   description='valid subcommands',
                                   help='description')


def init(args):
    print('Init')
    print(args)


def add(args):
    print('Add')
    print(args)


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


# Init parser
init_parser = subparsers.add_parser('init', help='Initial command')
init_parser.add_argument(
    '-q', '--quiet', default=True,
    metavar='quiet', dest='mode',
    help='initialize vcs in quiet mode'
)
init_parser.add_argument(
    '-b', '--branch',
    metavar='quiet', dest='branch',
    help='default branch name'
)
init_parser.set_defaults(func=init)

add_parser = subparsers.add_parser('add', help='Command to add files in tracked list')
add_parser.add_argument(
    '-f', '--file',
    metavar='filename', nargs='+', required=False,
    help='add(use . for add all files) file in a tracked list'
)
add_parser.add_argument(
    '-l', '--list',
    nargs='?', default=True,
    help='print list of tracked files'
)
add_parser.add_argument(
    '-c', '--clean',
    nargs='?', default=True,
    help='clean list of tracked files'
)
add_parser.add_argument(
    '-v', '--verbose',
    nargs='?', default=True,
    help='add files in tracked list in verbose mode'
)
# Error in flag -f
# add_parser.add_argument(
#     '-f', '--force',
#     nargs='?', default=True, required=False,
#     help='add files in tracked list in force mode'
# )
add_parser.set_defaults(func=add)

# Commit parser
commit_parser = subparsers.add_parser('commit', help='Command to commit changes')
commit_parser.add_argument(
    '-t', '--text',
    help='create commit with message', required=True
)
commit_parser.add_argument(
    '--HARD',
    nargs='?', default=True,
    help='commit in hard mode(remove previous commits)'
)
commit_parser.set_defaults(func=commit)

# Reset parser
reset_parser = subparsers.add_parser('reset', help='Command to reset last commit')
reset_parser.add_argument(
    '-v', '--verbose',
    nargs='?', default=True,
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
merge_parser.set_defaults(merge)

if __name__ == '__main__':
    args = parser.parse_args()
    if not vars(args):
        parser.print_usage()
    else:
        args.func(args)
