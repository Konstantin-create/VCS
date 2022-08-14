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
\
Print all commits in dir in verbose mode
```shell
~ python vcs.py log -a -v

be75a866de7cc4bcac6b6f76bdf4ee574bfc400a99646be48333b694566edc77
Commit: fe75d0eeb29a4e20f7f3888b32a0366326037ad742c45776ba4ee15846b64034
Message: Remove license
Time stamp: 2022-08-14 13:57:55.743984
Parent: 3f295f940632bcf145ffca60188f2d7bb9690b9e3fd039180cf53a898abe4111

Commit: 3f295f940632bcf145ffca60188f2d7bb9690b9e3fd039180cf53a898abe4111
Message: Remove license
Time stamp: 2022-08-14 13:14:37.634877
Parent: 8f4804cb84592f332a85cf5305222de3cf22d6ca0ff23020001a8b949b52f450

Commit: 8f4804cb84592f332a85cf5305222de3cf22d6ca0ff23020001a8b949b52f450
Message: Edit main.py
Time stamp: 2022-08-13 15:33:04.926488
Parent: 6ab6a9dbb43097b2d0a8737ce37f42e6419cca3b77dc1faabfa7ca2d816373ec

Commit: 6ab6a9dbb43097b2d0a8737ce37f42e6419cca3b77dc1faabfa7ca2d816373ec - Initial commit
Message: Initial commit
Time stamp: 2022-08-10 18:43:17.596296
Parent: Null

Total 5 commits found
```
## Help message
```shell

vcs log - Print last commit log
    -a | --all - Print all commits
    -v | --verbose - Be verbose
```
___

Author: [Konstantin-create](https://github.com/Konstantin-create)
\
Licence: [GNU General Public License v3.0](/LICENSE)

