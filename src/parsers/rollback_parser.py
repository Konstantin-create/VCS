from commands import Rollback
from .parser import subparsers

import os
from argparse import Namespace

def rollback_router(args: Namespace):
    """Handler for rollback parser"""

    rollback = Rollback(os.getcwd())
    rollback.rollback(verbose=args.verbose)
# Rollback parser
rollback_parser = subparsers.add_parser('rollback', help='Command to rollback to last commit')
rollback_parser.add_argument(
    '-v', '--verbose',
    action='store_true',
    dest='verbose',
    help='rollback to last commit in verbose mode'
)
rollback_parser.set_defaults(func=rollback_router)
