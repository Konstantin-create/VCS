# Branch command

Print list of branches
`vcs branch` is the same as `vcs branch -l | --list`

```shell
~ python vcs.py branch
Branches:
  master
  features
  test

Total 3 branches
```

\
Create new branch

```shell
~ python vcs.py -n test
Branch test has been created
4 files were inherited
```
\
Remove branch by name
```shell
~ python vcs.py -d test
Branch test was successfully deleted
```
___

## Help text

```shell
vcs branch - Print list of branches
vcs branch -l | --list - Print list of branches
vcs branch -n | --new <branch_name> - Create new branch
vcs branch -d | --delete <branch_name> - Remove branch
```

___

Author: [Konstantin-create](https://github.com/Konstantin-create)
\
Licence: [GNU General Public License v3.0](/LICENSE)