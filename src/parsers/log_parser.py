from commands import Log 
from .parser import subparsers

import os
from argparse import Namespace

def log_router(args: Namespace):
    """Handler for log parser"""

    log = Log(os.getcwd())
    if args.print_all:
        log.get_all_commits(bool(args.verbose))
        return
    log.get_commit_info(args.commit) if args.commit else log.get_commit_info()

# Log parser
log_parser = subparsers.add_parser('log', help='Command to print info about commits')
log_parser.add_argument(
    '-a', '--all',
    dest='print_all',
    action='store_true',
    help='print all commits'
)
log_parser.add_argument(
    '-v', '--verbose',
    dest='verbose',
    action='store_true',
    help='verbose mode'
)
log_parser.add_argument(
    '-c', '--commit',
    dest='commit',
    action='store_true',
    help='get commit info by hash'
)
log_parser.set_defaults(func=log_router)
