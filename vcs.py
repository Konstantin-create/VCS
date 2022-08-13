"""
Program init function
Functions:
    - Get command
    - Parse command
    - Call class/function from commands/ dir
"""

# Imports
from ast import arg
from tools import is_vcs_initialized
from tools import init_help, add_help, commit_help, ignore_help, vcs_help
from tools.flags_tools import *
from commands import *
from colorama import init, Fore

from tools.help_tools import log_help

# Colorama init
init(autoreset=True)

# Get run args
args = sys.argv


# Functions
def main():
    """Function to parse args and call the function"""
    cwd = os.getcwd()
    if args[1].lower() == 'init':
        quiet = False
        if '-quiet' in args or '-q' in args:
            quiet = True
        if '--help' in args or '-h' in args:
            init_help()
        elif '-b' in args:
            if len(args) <= args.index('-b') + 1:
                print(Fore.RED + 'If you gonna use -b flag - Branch name is required')
                sys.exit()
            Init(cwd, base_branch=args[args.index('-b') + 1], quiet=quiet)
        else:
            Init(cwd, quiet=quiet)

    else:
        if not is_vcs_initialized(cwd):
            print(Fore.RED + 'VCS is not initialized try "vcs init"')
            sys.exit()
        if args[1].lower() == 'add':
            if '--help' in args or '-h' in args:
                add_help()
            else:
                if len(args) <= args.index('add') + 1:
                    print(Fore.RED + 'File name or . | -A is required')
                    sys.exit()
                add = Add(cwd)
                if args[args.index('add') + 1] == '-l' or args[args.index('add') + 1] == '--list':
                    add.tracked_files_list()
                elif args[args.index('add') + 1] == '-c' or args[args.index('add') + 1] == '--clean':
                    print(Fore.YELLOW + 'Cleaning...')
                    add.tracked_files_clean()
                else:
                    verbose = False
                    force = False
                    if '-v' in args or '--verbose' in args:
                        verbose = True
                    if '-f' in args or '--force' in args:
                        force = True
                    add.add_tracked_file(args[args.index('add') + 1], verbose, force)

        elif args[1].lower() == 'commit':
            if '--help' in args or '-h' in args:
                commit_help()
            elif '-t' in args:
                if len(args) <= args.index('-t') + 1:
                    print(Fore.RED + 'Commit message is required')
                    sys.exit()

                if args[args.index('-t') + 1] not in commit_flags:
                    commit = Commit(cwd, args[args.index('-t') + 1])
                    if '--hard' in args or '--HARD' in args:
                        commit.hard_commit()
                    else:
                        commit.commit()
                else:
                    print(Fore.RED + 'Commit text error. Use "vcs commit --help" for help')
            else:
                print(Fore.RED + 'Command not found. User "vcs commit --help" for help')

        elif args[1].lower() == 'ignore':
            ignore = Ignore(cwd)
            if '-h' in args or '--help' in args:
                ignore_help()
            if '-tl' in args or '--template-list' in args:
                ignore.get_template_list()
            elif '-n' in args or '--new' in args:
                template = False
                if '-t' in args and len(args) >= args.index('-t') + 1:
                    template = args[args.index('-t') + 1]
                elif '--template' in args and len(args) >= args.index('--template') + 1:
                    template = args[args.index('--template') + 1]
                ignore.create_file(template=template)
            elif '-l' in args or '--list' in args:
                ignore.get_ignore_list()
        elif args[1].lower() == 'log':
            if '-h' in args or '--help' in args:
                log_help()
                sys.exit()
            log = Log(cwd)
            if '-a' in args or '--all' in args:
                log.get_all_commits()
            else:
                if len(args) >= 3:
                    log.get_commit_info(commit_hash=args[2])
                else:
                    log.get_commit_info()
        elif args[1].lower() == 'reset':
            verbose = False
            if '-v' in args or '--verbose' in args:
                verbose = True
            reset = Reset(cwd)
            reset.last_commit(verbose=verbose)
        elif args[1].lower() == '-h' or args[1].lower() == '--help':
            vcs_help()
        else:
            print(Fore.RED + f'No such command {args[1]}')


if __name__ == '__main__':
    main()
