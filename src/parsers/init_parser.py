from commands import Init
from .parser import subparsers

import os
from argparse import Namespace

def init_router(args: Namespace):
    """Handler for init parser"""

    Init(
        os.getcwd(),
        base_branch=args.branch or 'main',
        quiet=bool(args.quiet)
    )
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
