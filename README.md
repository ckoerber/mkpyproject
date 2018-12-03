# mkpyproject
Module for creating new python projects with a minimal amount of required files.

![Code demonstration](http://www.ckoerber.com/static/images/misc/mkpyproject-demo.gif)
## Install
Install via pip
```bash
pip install [-e] [--user] .
```

## Run
Once installed, the script can be run by
```bash
usage: mkpyproject [-h] [--author author] [--verbose] project_name

Create python project directory and supplemental files.

positional arguments:
  project_name          Name of the python project.

optional arguments:
  -h, --help            show this help message and exit
  --author author, -a author
                        Name of project author.
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
|--- notebooks/
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

## Contributing
See [Contributing.md](Contributing.md)

## License
See [LICENSE.md](LICENSE.md)
