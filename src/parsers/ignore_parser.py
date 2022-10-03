from commands import Ignore 
from .parser import subparsers

import os
from argparse import Namespace

def ignore_router(args: Namespace):
    """Handler for ignore parser"""

    ignore = Ignore(os.getcwd())
    if args.template_list:
        ignore.get_template_list()
        return
    if args.list:
        ignore.get_ignore_list()
        return
    if args.new:
        ignore.create_file(args.template)
# Ignore parser
ignore_parser = subparsers.add_parser('ignore', help='Command to modify ignore file')
ignore_parser.add_argument(
    '-tl', '--template-list',
    dest='template_list',
    action='store_true',
    help='print list  of templates'
)
ignore_parser.add_argument(
    '-l', '--list',
    dest='list',
    action='store_true',
    help='get list of ignores'
)
ignore_parser.add_argument(
    '-n', '--new',
    dest='new',
    help='create .ignore file with base ignores'
)
ignore_parser.add_argument(
    '-d', '--default',
    dest='default',
    help='create .ignore file with base ignores and template'
)
ignore_parser.set_defaults(func=ignore_router)

