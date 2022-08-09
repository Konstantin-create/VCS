# Ignore command

Base create .ignore with base ignores(like .git, .vcs, ect...)
```shell
~ python vcs.py ignore -n
.ignore file with base exceptions was created successfully
```
\
Create .ignore with base ignores and template
```shell
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
## Print template list
```shell
~ python vcs.py ignore -tl
Ignore templates list:
  python
  
Total 1 templates found
___

## Help message
```shell
vcs ignore 
    -n | --new - Create .ignore file with base ignores
    -t | --template - Create .ignore file with base ignores and template
vcs ignore -tl | --template-list - Print list  of templates
vcs ignore -l | --list - Get list of ignores
vcs ignore -h | --help - This help

```
___

Author: [Konstantin-create](https://github.com/Konstantin-create)
\
Licence: [GNU General Public License v3.0](/LICENSE)
