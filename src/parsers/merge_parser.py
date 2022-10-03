from commands import Merge
from .parser import subparsers

import os
from argparse import Namespace

def merge_router(args: Namespace):
    """Handler for merge parser"""

    merge = Merge(os.getcwd())
    merge.merge(args.branch_name)
# Merge parser
merge_parser = subparsers.add_parser('merge', help='Command to merge branches')
merge_parser.add_argument(
    'branch_name',
    help='merge branch_name with current branch in rebase mode'
)
merge_parser.set_defaults(func=merge_router)
