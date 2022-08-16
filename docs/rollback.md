# Rollback command

Base rollback command

```shell
python vcs.py rollback
Current commit: 8f4804cb84592f332a85cf5305222de3cf22d6ca0ff23020001a8b949b52f450
Rollback to commit: 6ab6a9dbb43097b2d0a8737ce37f42e6419cca3b77dc1faabfa7ca2d816373ec
Changes to rewrite: 4


Lucky rollback
```

\
Rollback in verbose mode

```shell
Current commit: 8f4804cb84592f332a85cf5305222de3cf22d6ca0ff23020001a8b949b52f450
Rollback to commit: 6ab6a9dbb43097b2d0a8737ce37f42e6419cca3b77dc1faabfa7ca2d816373ec
Changes to rewrite: 4

    File name: /.ignore
    File data hash: d023cff0b5960da265e890760c627c17ab9e7ae3bcfeeb30407455a050cd3290

    File name: /README.md
    File data hash: 362586bb07f6dbf334d5ba0c91623fc63b880a42db6f31125e97f68d2d7190cb

    File name: /LICENSE
    File data hash: d50c2d12a18d4bd006934cce09462a4e6c7292901884796776c43bc13b10becc

    File name: /main.py
    File data hash: bf2ea96c4d9f7d75061e82f8f138dbd779d982c1d9c770b8ada90af0d3974015


    File name: /.ignore
    File data hash: d023cff0b5960da265e890760c627c17ab9e7ae3bcfeeb30407455a050cd3290

    File name: /README.md
    File data hash: 362586bb07f6dbf334d5ba0c91623fc63b880a42db6f31125e97f68d2d7190cb

    File name: /LICENSE
    File data hash: d50c2d12a18d4bd006934cce09462a4e6c7292901884796776c43bc13b10becc

    File name: /main.py
    File data hash: bf2ea96c4d9f7d75061e82f8f138dbd779d982c1d9c770b8ada90af0d3974015

Lucky rollback
```

## Help message

```shell
vcs rollback - Rollback to last commit
vcs rollback -v | --verbose - Rollback to last commit in verbose mode
vcs reset -h | --help - This help
```

___

Author: [Konstantin-create](https://github.com/Konstantin-create)
\
Licence: [GNU General Public License v3.0](/LICENSE)
