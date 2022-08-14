# Init command

Base VCS init. Default branch name is `master`

```shell
~ python vcs.py init
/home/hacknet/Kostua/Python/VCS/.vcs/refs/heads/master

VCS initialized successfully
```

\
VCS init with custom branch name

```shell
~ python vcs.py init -b test
/home/hacknet/Kostua/Python/VCS/.vcs/refs/heads/test

VCS initialized successfully
```

\
VCS init in quiet mode

```shell
~ python vcs.py init -b master -q
```

___

## Help message

```shell
vcs init
    -b "<branch name>" - Create first branch with custom name
    -q | --quiet - Quiet mode. Only errors and warning
    -h | --help- This help
```

___

Author: [Konstantin-create](https://github.com/Konstantin-create)
\
Licence: [GNU General Public License v3.0](/LICENSE)

