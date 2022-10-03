from commands import Add 
from .parser import subparsers

import os
from argparse import Namespace

def add_router(args: Namespace):
    """Handler for add parser"""

    add = Add(os.getcwd())
    if args.list:
        add.tracked_files_list()
    elif args.clean:
        add.tracked_files_clean()
    else:
        for file in args.file:
            add.add_tracked_file(file, bool(args.verbose), bool(args.force))
# Add Parser
add_parser = subparsers.add_parser('add', help='Command to add files in tracked list')
add_parser.add_argument(  # todo: Replace with subparser. Remove flag -f
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
