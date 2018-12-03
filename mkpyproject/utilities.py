"""Utility functions for mkpyproject
"""
from typing import Optional
import os

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
FILES_DIR = os.path.join(FILE_DIR, "files")


def write_file(
    dir_name: str,
    file_name: str,
    content: Optional[str] = None,
    overwrite: bool = False,
):
    """Writes content to file.

    Arguments
    ---------

    Raises
    ------
    """
    if not os.path.exists(dir_name):
        raise ValueError(f"Directory '{dir_name}' does not exist.")

    file_dir = os.path.join(dir_name, file_name)

    if os.path.exists(file_dir) and not overwrite:
        raise ValueError(f"File '{file_dir}' exists and overwrite is turned off.")

    content = content or ""
    with open(file_dir, "w") as out:
        out.write(content)


def make_project_dirs(project_name: str) -> None:
    """Creates project directories
    """
    os.mkdir(project_name)

    for dir_name in [project_name, "tests"]:
        this_dir = os.path.join(project_name, dir_name)
        os.mkdir(this_dir)
        write_file(this_dir, "__init__.py")

    for dir_name in ["notebooks", "docs"]:
        this_dir = os.path.join(project_name, dir_name)
        os.mkdir(this_dir)


def write_license(
    directory: str,
    license_kind: str = "MIT",
    author: Optional[str] = None,
    year: Optional[int] = None,
) -> None:
    """Writes license into project root directory
    """
    if license_kind == "MIT":
        with open(os.path.join(FILES_DIR, "LICENSE-MIT.md"), "r") as inp:
            license_text = inp.read()
    else:
        raise ValueError("Unknown license '{license_kind}'.")

    if author:
        license_text = license_text.replace("{COPYRIGHT HOLDER}", author)
    if year:
        license_text = license_text.replace("{YEAR}", year)

    write_file(directory, "LICENSE.md", license_text)


def write_gitignore(project_name: str):
    """
    """
    with open(os.path.join(FILES_DIR, ".gitignore"), "r") as inp:
        gitignore_text = inp.read()
    write_file(project_name, ".gitignore", gitignore_text)


def write_requirements(project_name: str):
    """
    """
    write_file(project_name, "requirements.txt")


def write_setup(project_name: str):
    """
    """
    with open(os.path.join(FILES_DIR, "setup.py"), "r") as inp:
        setup_text = inp.read()
    write_file(project_name, "setup.py", setup_text)


def write_readme(project_name: str):
    """
    """
    with open(os.path.join(FILES_DIR, "README.md"), "r") as inp:
        readme_text = inp.read()
    write_file(project_name, "README.md", readme_text)
