# Add command

## Add files
\
Add all files in current folder to tracked list
```shell
~ python vcs.py add .

Found 3 ignores
12 were added to tracked list
Files were successfully added to tracked list
```
or
```shell
~ python vcs.py add -A

Found 3 ignores
12 were added to tracked list
Files were successfully added to tracked list
```
\
Add one file from current folder to traked list
```shell
~ python vcs.py add file_name.example

Found 3 ignores
1 was added to tracked list
Files were successfully added to tracked list
```
\
Add files and be verbose
```shell
~ python ../vcs.py add . -v

Found 4 ignores
Added files:
    /main.py - f44014d759c159acba60a8d99a5512f81bb62f994ac877693aed43cd9da00e50
    /LICENSE - 12de9234cb2d3793b126aba8704eacc890a685f6f163b6c1a784afd1f9f26b48
    /.ignore - 56fedfcbc4dcd01138579f78f18d2a8be5b79ba7b51bfadaa0da860d55fca7bb
    /README.md - 95e0a42d9d6b5d82bdb3752f4d31f3fe7d0150c6b512bc094985b1a2b24b192b

4 were added to tracked list
Files were successfully added to tracked list
```
\
Disregard .ignore file
```shell
~ python ../vcs.py add . -v -f
Force mode. .ignore file will not be read
Added files:
    /main.py - f44014d759c159acba60a8d99a5512f81bb62f994ac877693aed43cd9da00e50
    /LICENSE - 12de9234cb2d3793b126aba8704eacc890a685f6f163b6c1a784afd1f9f26b48
    /.ignore - 56fedfcbc4dcd01138579f78f18d2a8be5b79ba7b51bfadaa0da860d55fca7bb
    /README.md - 95e0a42d9d6b5d82bdb3752f4d31f3fe7d0150c6b512bc094985b1a2b24b192b
    /.vcs/CURRENT_BRANCH - 5c014d11cff2df9a86ea2cd755dab48199e8d6477a46ee3a38f7f6e54e625140
    /.vcs/config.json - 14ab13a54d3684d7fc635d5fc9f3dd20efb93c5f5a284fb77d34aa15b6014b87
    /.vcs/tracked_files.json - 5ef89ec7a2a4ff9a55b9718ab4d663203290dc779168e960046fa8b83e2e0e21

7 were added to tracked list
Files were successfully added to tracked list
```

___

## Print current tracked files list


```shell
Traking files:
    /LICENSE
    /README.md
    /.ignore
    /requirements.txt
    /vcs.py
    /commands/__init__.py
    /commands/init_function.py
    /commands/add_function.py
    /tools/file_tools.py
    /tools/__init__.py
    /tools/ignore_tools.py
    /docs/img/init_function.png
```

___

## Help message:
```shell
vcs add <file_name> | . | -A
    . = -A - Add all files in current directory to tracked files list
vcs add
    -l - Print all tracked files list
    -c | --clean - Clear tracked files list
    -v | --verbose - Be verbose
    -f | --force - Disregard .ignore file
    -h | --help - This help
```

___

Author: [Konstantin-create](https://github.com/Konstantin-create)
\
Licence: [GNU General Public License v3.0](/LICENSE)

