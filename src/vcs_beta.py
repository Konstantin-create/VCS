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

if __name__ == '__main__':
    args = parser.parse_args()
    if not vars(args):
        parser.print_usage()
    else:
        args.func(args)
