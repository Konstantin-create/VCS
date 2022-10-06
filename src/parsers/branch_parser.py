from commands import Branch 
from .parser import subparsers

import os
from argparse import Namespace

def branch_router(args: Namespace):
    """Handler for branch parser"""

    branch = Branch(os.getcwd())
    if args.list:
        branch.branches_list()
        return
    if args.new:
        branch.create_new(args.new)
        return
    if args.delete:
        branch.remove_branch(args.delete, bool(args.force))
# Branch parser
branch_parser = subparsers.add_parser('branch', help='Command to modify branches')
branch_parser.add_argument(
    '-l', '--list',
    action='store_true',
    dest='list',
    help='command to modify branches'
)
branch_parser.add_argument(
    '-n', '--new',
    dest='new',
    help='create new branch'
)
branch_parser.add_argument(
    '-d', '--delete',
    dest='delete',
    help='remove branch'
)
branch_parser.add_argument(
    '-f', '--force',
    dest='force',
    action='store_true',
    help='remove branch in a force mode'
)
branch_parser.set_defaults(func=branch_router)
