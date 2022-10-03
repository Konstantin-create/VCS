from commands import Reset 
from .parser import subparsers

import os
from argparse import Namespace

def reset_router(args: Namespace):
    """Handler for reset parser"""

    reset = Reset(os.getcwd())
    reset.last_commit(verbose=bool(args.verbose))

# Reset parser
reset_parser = subparsers.add_parser('reset', help='Command to reset last commit')
reset_parser.add_argument(
    '-v', '--verbose',
    action='store_true',
    dest='verbose',
    help='rollback to last commit in verbose mode'
)
reset_parser.set_defaults(func=reset_router)
