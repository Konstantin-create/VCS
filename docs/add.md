# Add command

## Add files
\
Add all files in current folder to tracked list
```diff
~ python vcs.py add .

Found 3 ignores
12 were added to tracked list
Files were successfully added to tracked list
```
or
```diff
~ python vcs.py add -A

Found 3 ignores
12 were added to tracked list
Files were successfully added to tracked list
```
\
Add one file from current folder to traked list
```diff
~ python vcs.py add file_name.example

Found 3 ignores
1 was added to tracked list
Files were successfully added to tracked list
```
___
## Print current tracked files list


```diff
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

Author: [Konstantin-create](https://github.com/Konstantin-create)
\
Licence: [GNU General Public License v3.0](/LICENSE)

