# -*- coding: utf-8 -*-
"""Setup file for {project_name}
"""
__author__ = "{author}"
__version__ = "0.1.0"

from os import path

from setuptools import setup, find_packages

CWD = path.abspath(path.dirname(__file__))

with open(path.join(CWD, "README.md"), encoding="utf-8") as inp:
    LONG_DESCRIPTION = inp.read()

with open(path.join(CWD, "requirements.txt"), encoding="utf-8") as inp:
    REQUIREMENTS = [el.strip() for el in inp.read().split(",")]

setup(
    name="{project_name}",
    version=__version__,
    description=None,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url=None,
    author=__author__,
    author_email=None,
    keywords=[],
    packages=find_packages(exclude=["docs", "tests"]),
    install_requires=REQUIREMENTS,
)
