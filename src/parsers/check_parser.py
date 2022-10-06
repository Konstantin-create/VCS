from commands import Checker 
from .parser import subparsers

import os
from argparse import Namespace


def check_router(args: Namespace):
    """Handler for check parser"""

    checker = Checker(os.getcwd())
    if args.commits:
        checker.check_commits_chain()
    if args.branches:
        checker.check_branches()

# Check parser
check_parser = subparsers.add_parser('check', help='Command to check vcs state')
check_parser.add_argument(
    '-c', '--commits',
    dest='commits',
    action='store_true',
    help='command to check vcs state'
)
check_parser.add_argument(
    '-b', '--branches',
    dest='branches',
    action='store_true',
    help='check is branches valid'
)
check_parser.set_defaults(func=check_router)
