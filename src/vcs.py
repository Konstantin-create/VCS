"""
Parser for commands:
    - Init command(init_router)
    - Add command(add_router)
    - Commit command(commit_router)

    - Reset command(reset_router)
    - Rollback command(rollback_router)

    - Checkout command(checkout_router)
    - Branch command(branch_router)
    - Merge command(merge_router)

    - Ignore command(ignore_router)
    - Log command(log_parser)
    - Status command(status_command)
    - Check command(check_command)
"""
from commands import *
from parsers.parser import parser
import parsers # Inits all commands(DO NOT TOUCH)

if __name__ == '__main__':
    args = parser.parse_args()
    if not vars(args):
        parser.print_usage()
    else:
        args.func(args)
