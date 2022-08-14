# Commit command

<br>
Output from commit command have some color indications:

- [master <span style="color: green">815567</span>] `<Commit text>` - Green - Initial commit
- [master <span style="color: orange">815567</span>] `<Commit text>` - Yellow - Child commit
- [master <span style="color: red">815567</span>] `<Commit text>` - Red - Hard reset commit

___

Base commit example

```shell
~ python vcs.py commit -t "Initial commit"
[master 815567] Initial commit
 1 have been objects created
```

Commit with remove commits history

```shell
~ python vcs.py commit -t "Hard reset commit" --hard
[main 9c4138] Hard reset commit
 1 have been objects created
```

___

## Help message

```shell
vcs commit -t "<Your commit text>" - Create commit with text
vcs commit -t "<Your commit text>" - Create commit, and remove all previous commits
vcs commit -h | --help - This help
```

___

Author: [Konstantin-create](https://github.com/Konstantin-create)
\
Licence: [GNU General Public License v3.0](/LICENSE)

