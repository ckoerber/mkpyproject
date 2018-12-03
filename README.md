# mkpyproject
Module for creating new python projects with a minimal amount of required files.

## Description

## Install
Install via pip
```bash
pip install [-e] [--user] .
```

## Run
Once installed, the script can be run by
```bash
usage: mkpyproject [-h] [--name project_name] [--verbose]

Create python project directory and supplemental files.

optional arguments:
  -h, --help            show this help message and exit
  --name project_name, -n project_name
                        Name of the python project.
  --verbose, -v         Allow verbose output.
```
This will create the python directory structure
```bash
project_name/
|--- project_name/
|    |--- __init__.py
|
|--- tests/
|    |--- __init__.py
|
|--- docs/
|--- requirements.txt
|--- LICENSE.md
|--- README.md
|--- setup.py
|--- .gitignore
```
in the current directory.
Some files like `setup.py` come with predefined standard values.

## Authors
* Christopher Körber

## Contribute

## License
See [LICENSE.md](LICENSE.md)
