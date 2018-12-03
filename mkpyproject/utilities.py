# -*- coding: utf-8 -*-
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
        dir_name: str
            The directory of the file.

        file_name: str
            The name of the file (including extension).

        content: str
            The content of the file.

        overwrite: bool
            Overwrites file if it already exists, otherwise raises exception.

    Raises
    ------
        FileNotFoundError:
            If the directory does not exist.

        FileExistsError:
            File exists and `overwrite` is False.
    """
    if not os.path.exists(dir_name):
        raise FileNotFoundError(f"Directory '{dir_name}' does not exist.")

    file_dir = os.path.join(dir_name, file_name)

    if os.path.exists(file_dir) and not overwrite:
        raise ValueError(f"File '{file_dir}' exists and overwrite is turned off.")

    content = content or ""
    with open(file_dir, "w") as out:
        out.write(content)


class PyProject:
    """Project class for creating predefined folders and writing files.
    """

    def __init__(
        self,
        project_name: str,
        author: Optional[str] = None,
        verbose: Optional[int] = 0,
    ) -> None:
        """Initializes a project with a given name and author

            Arguments
            ---------
                project_name: str
                    Name of the python project.


                author: str
                    Name of the project author.

                verbose: int
                    Print additional output if `verbose > 0`.
        """
        self.project_name = project_name
        self.author = author
        self.verbose = verbose

    def make_project_dirs(self) -> None:
        """Creates project directories.

        Creates the project directories
        """
        if not self.project_name.isidentifier():
            raise ValueError(
                "Project name must fulfill PEP8"
                " (`self.project_name.isidentifier() == True`)"
            )

        os.mkdir(self.project_name)

        for dir_name in [self.project_name, "tests"]:
            this_dir = os.path.join(self.project_name, dir_name)
            os.mkdir(this_dir)
            write_file(this_dir, "__init__.py")

        for dir_name in ["notebooks", "docs"]:
            this_dir = os.path.join(self.project_name, dir_name)
            os.mkdir(this_dir)

    def write_license(
        self, license_kind: str = "MIT", year: Optional[int] = None
    ) -> None:
        """Creates file 'LICENSE.md' in project root.

        Imports information from 'files/LICENSE-{license_kind}.md' and substitudes
        project author and year if possible.

        Arguments
        ---------
            license_kind: str
                Kind of license. Currently only 'MIT' is implemented.

            year: int
                Year of the copyright. If `None` year will be the current year.
        """
        if license_kind == "MIT":
            with open(os.path.join(FILES_DIR, "LICENSE-MIT.md"), "r") as inp:
                license_text = inp.read()
        else:
            raise ValueError("Unknown license '{license_kind}'.")

        if self.author:
            license_text = license_text.replace("{COPYRIGHT HOLDER}", self.author)
        if year:
            license_text = license_text.replace("{YEAR}", str(year))

        write_file(self.project_name, "LICENSE.md", license_text)

    def write_gitignore(self):
        """Creates file '.gitignore' in project root.

        Imports information from 'files/.gitignore'.
        """
        with open(os.path.join(FILES_DIR, ".gitignore"), "r") as inp:
            gitignore_text = inp.read()
        write_file(self.project_name, ".gitignore", gitignore_text)

    def write_requirements(self):
        """Creates empty file 'requirements.txt' in project root.
        """
        write_file(self.project_name, "requirements.txt")

    def write_setup(self):
        """Creates file 'setup.py' in project root.

        Imports information from 'files/setup.py' and substitudes project name and
        author if possible.
        """
        with open(os.path.join(FILES_DIR, "setup.py"), "r") as inp:
            setup_text = inp.read()

        setup_text = setup_text.replace(r"{project_name}", self.project_name)
        setup_text = setup_text.replace("{author}", self.author)

        write_file(self.project_name, "setup.py", setup_text)

    def write_readme(self):
        """Creates file 'README.md' in project root.

        Imports information from 'files/README.md' and substitudes project name and
        author if possible.
        """
        with open(os.path.join(FILES_DIR, "README.md"), "r") as inp:
            readme_text = inp.read()

        print(readme_text)
        readme_text = readme_text.replace(r"{project_name}", self.project_name)
        if self.author:
            readme_text = readme_text.replace("{author}", self.author)

        write_file(self.project_name, "README.md", readme_text)
