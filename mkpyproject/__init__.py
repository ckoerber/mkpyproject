# -*- coding: utf-8 -*-
"""Script to create python projects and required files
"""
import argparse

from mkpyproject.utilities import PyProject


def main() -> int:
    """Creates directories and files for the new python project.
    """
    parser = argparse.ArgumentParser(
        description="Create python project directory and supplemental files."
    )
    parser.add_argument(
        "--name",
        "-n",
        metavar="project_name",
        help="Name of the python project.",
        type=str,
    )
    parser.add_argument("--verbose", "-v", action="count", help="Allow verbose output.")

    args = parser.parse_args()

    this_project = PyProject(args.project_name, args.author)

    this_project.make_project_dirs()
    this_project.write_license("MIT")
    this_project.write_gitignore()
    this_project.write_requirements()
    this_project.write_setup()
    this_project.write_readme()
