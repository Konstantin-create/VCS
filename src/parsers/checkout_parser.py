from commands import CheckOut 
from .parser import subparsers

import os
from argparse import Namespace

def checkout_router(args: Namespace):
    """Handler for checkout parser"""

    checkout = CheckOut(os.getcwd())
    checkout.checkout(args.branch, create_new_branch=bool(args.new))

# Checkout parser
checkout_parser = subparsers.add_parser('checkout',
                                        help='Switch branches')  # todo: rewrite with subparser(remove flags -b and -n)
checkout_parser.add_argument(
    '-b', '--branch',
    dest='branch',
    help='switch branch'
)
checkout_parser.add_argument(
    '-n', '--new',
    dest='new',
    help='create branch and switch'
)
checkout_parser.set_defaults(func=checkout_router)
