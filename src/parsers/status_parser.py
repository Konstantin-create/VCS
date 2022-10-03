from commands import Status
from .parser import subparsers

import os
from argparse import Namespace

def status_router(args: Namespace):
    """Handler for status parser"""

    status = Status(os.getcwd())
    status.status()
# Status parser
status_parser = subparsers.add_parser('status', help='command to print current vcs status')
status_parser.add_argument(
    ' ',
    nargs='?', default=True,
    help='base command to print status'
)
status_parser.set_defaults(func=status_router)
