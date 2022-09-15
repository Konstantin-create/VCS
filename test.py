import argparse

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(title='subcommands',
                                   description='valid subcommands',
                                   help='description')


def init(args):
    print('Init')
    print(args)


def add(args):
    print('Add')
    print(args)


create_parser = subparsers.add_parser('init', help='Initial command')
create_parser.add_argument('-q', '--quiet', metavar='quiet', dest='mode', help='initialize vcs in quiet mode')
create_parser.add_argument('-b', '--branch', dest='branch', help='default branch name')
create_parser.set_defaults(func=init)

add_parser = subparsers.add_parser('add', help='add data to db')
add_parser.add_argument('filename', nargs='+', help='add(use . for add all files) file in a tracked list')
add_parser.add_argument('-l', '--list', dest='mode', help='list of tracked files')
add_parser.add_argument('-c', '--clean', dest='mode',
                        help='clean tracked files list')
add_parser.set_defaults(func=add)

if __name__ == '__main__':
    args = parser.parse_args()
    if not vars(args):
        parser.print_usage()
    else:
        args.func(args)
