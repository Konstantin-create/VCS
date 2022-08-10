# Log command

Print last commit log
```shell
~ python vcs.py log
    Commit: 39458c22432915f28ca4f99e5fa29a8e7b9b65c74d5b3a4c76b86de24f82ee1b
    Message: Initial
    Time stamp: 2022-08-09 18:06:39.970791
    Parent: None
```
\
Print commit by commit hash
```shell
~ python vcs.py log <commit_hash>
    Commit: 39458c22432915f28ca4f99e5fa29a8e7b9b65c74d5b3a4c76b86de24f82ee1b
    Message: Initial
    Time stamp: 2022-08-09 18:06:39.970791
    Parent: None
```
\
Print all commits in dir
```shell
~ python vcs.py log -a

82e9945d440a48127ce9cedcc7b31f26319535ed79bed0f0bf2cb784e169bfca
75eaae1c63a01b7c9cf3c0913e958ffc87642531a5c35ff42f54ba03f7dbea5c
6ab6a9dbb43097b2d0a8737ce37f42e6419cca3b77dc1faabfa7ca2d816373ec - Initial commit

Total 3 commits found
```
## Help message
```shell
vcs log - Print last commit log
vcs log -a | --all - Print all commits
```
___

Author: [Konstantin-create](https://github.com/Konstantin-create)
\
Licence: [GNU General Public License v3.0](/LICENSE)

