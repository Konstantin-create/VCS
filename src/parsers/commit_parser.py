from commands import Commit
from .parser import subparsers

import os
from argparse import Namespace

def commit_router(args: Namespace):
    """Handler for commit parser"""

    commit = Commit(os.getcwd(), args.text)
    commit.hard_commit() if args.hard else commit.commit()
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
