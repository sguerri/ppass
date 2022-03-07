# Copyright (C) 2022 Sebastien Guerri
#
# This file is part of ppass.
#
# ppass is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# ppass is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""Handle git actions
"""

import subprocess


class git:
    """Static class for git actions
    """

    @staticmethod
    def status(path: str):
        """Return git status

        Args:
            path (str): working directory
        """
        subprocess.run(["git", "-C", path, "status"])

    @staticmethod
    def init(path: str, repo: str, branch: str, user: str, mail: str, pull: bool = False):
        """Initialise working directory

        Args:
            path (str): working directory
            repo (str): remote git repository
            branch (str): remote git repository branch
            user (str): remote git repository user
            mail (str): remote git repository email
            pull (bool, optional): If True, pull git repo instead of creating a new one. Defaults to False.
        """
        subprocess.run(["git", "-C", path, "init"], capture_output=True)
        subprocess.run(["git", "-C", path, "config", "user.name", user], capture_output=True)
        subprocess.run(["git", "-C", path, "config", "user.email", mail], capture_output=True)
        subprocess.run(["git", "-C", path, "remote", "add", "origin", repo], capture_output=True)
        if pull:
            git.pull(path)
        else:
            git.push(path, "Initial commit", branch)

    @staticmethod
    def pull(path: str):
        """Pull remote repository

        Args:
            path (str): working directory
        """
        subprocess.run(["git", "-C", path, "pull"])

    @staticmethod
    def push(path: str, message: str, branch: str):
        """Commit and push changes to remote

        Args:
            path (str): working directory
            message (str): commit message
            branch (str): commit branch
        """
        subprocess.run(["git", "-C", path, "add", "."], capture_output=True)
        subprocess.run(["git", "-C", path, "commit", "-m", message], capture_output=True)
        subprocess.run(["git", "-C", path, "push", "origin", branch])
