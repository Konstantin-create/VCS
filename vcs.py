"""
Program init function
Functions:
    - Get command
    - Parse command
    - Call class/function from commands/ dir
"""

# Imports
from commands import *
from tools.help_tools import *
from tools.flags_tools import *
from colorama import init, Fore
from tools import is_vcs_initialized
from tools.help_tools import log_help

# Colorama init
init(autoreset=True)

# Get run args
args = sys.argv


# Functions
def main():
    """Function to parse args and call the function"""

    cwd = os.getcwd()
    if not len(args) - 1:
        vcs_help()
        return

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
                verbose = False
                if '-v' in args or '--verbose' in args:
                    verbose = True
                log.get_all_commits(verbose)
            else:
                if len(args) >= 3:
                    log.get_commit_info(commit_hash=args[2])
                else:
                    log.get_commit_info()

        elif args[1].lower() == 'reset':
            if '-h' in args or '--help' in args:
                reset_help()
                return

            verbose = False
            if '-v' in args or '--verbose' in args:
                verbose = True
            reset = Reset(cwd)
            reset.last_commit(verbose=verbose)

        elif args[1].lower() == 'rollback':
            if '-h' in args or '--help' in args:
                rollback_help()
                return

            verbose = False
            if '-v' in args or '--verbose' in args:
                verbose = True
            rollback = Rollback(cwd)
            rollback.rollback(verbose)

        elif args[1].lower() == 'status':
            if '-h' in args or '--help' in args:
                status_help()
                return
            status = Status(cwd)
            status.status()

        elif args[1].lower() == 'checkout':
            if '-h' in args or '--help' in args:
                checkout_help()
                return

            branch_name = ''
            create_new = False
            if len(args) >= 3 and args[2] not in checkout_flags:  # todo: rewrite on switch cases
                branch_name = args[2]
            elif '-b' in args or '--branch' in args:
                if '-b' in args:
                    branch_flag = '-b'
                else:
                    branch_flag = '--branch'

                if len(args) <= args.index(branch_flag):
                    print(Fore.RED + 'No branch name found. Try "vcs checkout -h | --help"')
                    return
                branch_name = args[args.index(branch_flag) + 1]
                create_new = True
            if not len(branch_name):
                print(Fore.RED + 'No branch name found. Try "vcs checkout -h | --help"')
                return

            checkout = CheckOut(cwd)
            checkout.checkout(branch_name, create_new_branch=create_new)

        elif args[1] == 'branch':
            if '-h' in args or '--help' in args:
                branch_help()
                return
            branch = Branch(cwd)

            if '-l' in args or '--list' in args or len(args) == 2:
                branch.branches_list()
                return
            elif '-n' in args or '--new' in args:
                if '-n' in args:
                    command_flag = '-n'
                else:
                    command_flag = '--new'
                if len(args) <= args.index(command_flag) or args[args.index(command_flag) + 1] in branch_flags:
                    print(Fore.RED + 'Branch name not found')
                    return
                branch.create_new(args[args.index(command_flag) + 1])

            elif '-d' in args or '--delete' in args:
                command_flag = ''
                force = False

                if '-d' in args:
                    command_flag = '-d'
                else:
                    command_flag = '--delete'

                if len(args) <= args.index(command_flag) or args[args.index(command_flag) + 1] in branch_flags:
                    print(Fore.RED + 'Branch name not found')
                    return
                if '-f' in args or '--force' in args:
                    force = True
                branch.remove_branch(args[args.index(command_flag) + 1], force=force)

        elif args[1].lower() == '-h' or args[1].lower() == '--help':
            vcs_help()

        else:
            print(Fore.RED + f'No such command {args[1]}')


if __name__ == '__main__':
    main()
