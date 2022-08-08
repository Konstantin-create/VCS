# Ignore command

Base create with base ignores(like .git, .vcs, ect...)
```shell
~ python vcs.py ignore -n
.ignore file with base exceptions was created successfully
```

## Print all exeptions from .ignore file
```shell
~ python vcs.py ignore -l
Ignores:
  /.git
  /.vcs/

Total 2 ignores
```
___

## Help message
```shell
vcs ignore -n | --new - Create .ignore file with base ignores
vcs ignore -l | --list - Get list of ignores
vcs ignore -h | --help - This help
```
___

Author: [Konstantin-create](https://github.com/Konstantin-create)
\
Licence: [GNU General Public License v3.0](/LICENSE)
