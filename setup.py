"""Setup file for mkpyproject

See also https://github.com/pypa/sampleproject
"""
__author__ = "Christopher Koerber"
__version__ = "0.1"

from os import path

from setuptools import setup, find_packages

CWD = path.abspath(path.dirname(__file__))

with open(path.join(CWD, "README.md"), encoding="utf-8") as inp:
    LONG_DESCRIPTION = inp.read()

with open(path.join(CWD, "requirements.txt"), encoding="utf-8") as inp:
    REQUIREMENTS = [el.strip() for el in inp.read().split(",")]

setup(
    name="mkpyproject",
    version=__version__,
    description="Create new python projects from command line.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url=None,
    author=__author__,
    author_email="christopher@ckoerber.com",
    keywords="python setuptools development",
    packages=find_packages(exclude=["docs", "tests"]),
    install_requires=REQUIREMENTS,
    data_files=[("files", ["mkpyproject/files"])],
    entry_points={"console_scripts": ["mkpyproject=mkpyproject:main"]},
)
