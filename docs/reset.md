# Reset command

Base reset command
```shell
~ python vcs.py reset
Rollback to commit 6ab6a9dbb43097b2d0a8737ce37f42e6419cca3b77dc1faabfa7ca2d816373ec
Changes to rewrite: 4

Lucky rollback
```
\
Reset command in verbose mode
```shell
Rollback to commit 6ab6a9dbb43097b2d0a8737ce37f42e6419cca3b77dc1faabfa7ca2d816373ec
Changes to rewrite: 4

    File name: /.ignore
    File data hash: d023cff0b5960da265e890760c627c17ab9e7ae3bcfeeb30407455a050cd3290

    File name: /README.md
    File data hash: 362586bb07f6dbf334d5ba0c91623fc63b880a42db6f31125e97f68d2d7190cb

    File name: /LICENSE
    File data hash: d50c2d12a18d4bd006934cce09462a4e6c7292901884796776c43bc13b10becc

    File name: /main.py
    File data hash: e1c09db48437385e94817a7e4b2a9c65da9bafb677babc54142ecb9fce79bec5

Lucky rollback
```

## Help message
```shell
vcs reset - Reset to last commit
vcs reset -v | --verbose - Reset to last commit in verbose mode
vcs reset -h | --help
```

___

Author: [Konstantin-create](https://github.com/Konstantin-create)
\
Licence: [GNU General Public License v3.0](/LICENSE)
