"""Script to create python projects and required files
"""
import argparse

import mkpyproject.utilities as ut


def main() -> int:
    """Creates directories and files for the new python project
    """
    parser = argparse.ArgumentParser(
        description="Create python project directory and supplemental files."
    )
    parser.add_argument(
        "--name",
        "-n",
        metavar="project_name",
        help="Name of the python project",
        type=str,
    )
    parser.add_argument(
        "--verbose", "-v", action="count", help="Allow descriptional output"
    )

    args = parser.parse_args()
    print(args.project_name, args.verbose)

    ut.make_project_dirs(args.project_name)
    ut.write_license(args.project_name, "MIT")
    ut.write_gitignore(args.project_name)
    ut.write_requirements(args.project_name)
    ut.write_setup(args.project_name)
    ut.write_readme(args.project_name)

    return 1
