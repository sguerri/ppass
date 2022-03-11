# Welcome to ppass

[![](https://badgen.net/github/release/sguerri/ppass)](https://github.com/sguerri/ppass/releases/)
[![](https://img.shields.io/github/workflow/status/sguerri/ppass/Build/v1.2.0)](https://github.com/sguerri/ppass/actions/workflows/build.yml)
[![](https://badgen.net/github/license/sguerri/ppass)](https://www.gnu.org/licenses/)
[![](https://badgen.net/pypi/v/ppass)](https://pypi.org/project/ppass/)
[![](https://badgen.net/pypi/python/ppass)](#)
[![](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](#)

> GPG Password Manager

**ppass** is heavily inspired from **[pass](https://www.passwordstore.org/)**

I wanted to extend some of its functionnalities, and decided to rewrite the application in Python. It was a good exercice to try Python as I am more used to program in js/ts and c++/qt.

This beeing said, **ppass** is not as well tested or stable as **[pass](https://www.passwordstore.org/)**. I intend to make it evolve in the future, as I am using it on a daily basis. I am however alone on this one. If you want stability and portability, with a great community, please use **[pass](https://www.passwordstore.org/)**.

Stores created with **ppass** are compatible with **[pass](https://www.passwordstore.org/)**. They are thus also compatible with pass clients like [Android Password Store](https://github.com/android-password-store/Android-Password-Store#readme).


**Main features**
* gpg password creation (one file per password)
* enhanced password file with username, url and comments
* open web browser from password file
* automatic fill in username and password to web browser
* automatic ssh connexion with username and password
* cli commands shortcuts for fast access to passwords
* git integration
* possibility to handle several distinct stores
* commands and params autocompletion
* cli user interface or json response

**Roadmap**
* enhanced filter
* enhanced clip functionnality
* test on other platforms
* code cleaning
* more to come...

---

- [Welcome to ppass](#welcome-to-ppass)
  * [Installation](#installation)
    + [Requirements](#requirements)
    + [Install from pypi](#install-from-pypi)
    + [Install from deb package](#install-from-deb-package)
  * [Usage](#usage)
    + [Initialise](#initialise)
    + [Create a folder](#create-a-folder)
    + [Create a new password](#create-a-new-password)
    + [Clip username and password](#clip-username-and-password)
    + [Filter](#filter)
    + [Add a new store](#add-a-new-store)
    + [Use a store](#use-a-store)
    + [Initialise new git repository](#initialise-new-git-repository)
    + [Initialise from existing git repository](#initialise-from-existing-git-repository)
    + [Publish to git](#publish-to-git)
    + [Change output to JSON](#change-output-to-json)
    + [Shortcuts and Aliases](#shortcuts-and-aliases)
  * [SSH Connexion](#ssh-connexion)
  * [Build](#build)
  * [Dependencies](#dependencies)
  * [Author](#author)
  * [Issues](#issues)
  * [License](#license)

## Installation

### Requirements

The application is developped and used on ubuntu 21.10, with python 3.9.7. Any feedback on other platforms is welcomed.

- python3 >=3.6.2,<4.0
- xdotool: `sudo apt install xdotool`
- git: `sudo apt install git`
- gpg: `sudo apt install gnupg`
- nano: `sudo apt install nano`
- xclip: `sudo apt install xclip`

### Install from pypi

```bash
pip install ppass
```

For an isolated environment with [pipx](https://pypa.github.io/pipx/):

```bash
pipx install ppass
```

### Install from deb package

A deb package is available, built using `dh-virtualenv`. Installing this package will create a new Python virtual environment in `opt/venvs`. It will then create the symlink `usr/bin/ppass` pointing to `opt/venvs/ppass/bin/ppass`.

Note that `dh-virtualenv` built packages are dependent of python version. Use this only if you have default python version installed:
* ubuntu bionic 18.04: Python 3.6
* ubuntu focal 20.04: Python 3.8
* ubuntu hirsute 21.04: Python 3.9
* ubuntu impish 21.10: Python 3.9

Download latest `.deb` file from the [release page](https://github.com/sguerri/ppass/releases).

```bash
sudo dpkg -i ppass_1.2.0_{{os}}_amd64.deb
```

## Usage

### Initialise

Initialisation is required before using the application, to select GPG identity.

```bash
ppass init
```

A configuration file `.ppassrc` is created in the user home directory.

By default, passwords will be stored in `${HOME}/.ppass/` folder.

The `--edit` option will open configuration file in edit mode.

### Create a folder

A folder needs to be created before creating a password file.

```bash
ppass folders create

# or

ppass folders create --name "${NAME}"
```

### Create a new password

You can then create a new password file.

If you want a new password to be generated:

```bash
ppass generate
```

If you already know the password:

```bash
ppass insert
```

If the is only one folder, it will be selected by default. Otherwise the list of available folders will be prompted for selection.

### Clip username and password

`ppass open` will open a new webbrowser with the saved url

`ppass clip` will copy and paste to the active window the username as well as the password : `{username} {TAB} {password} {RETURN}`

`ppass user` will copy username to clipboard

`ppass pass` will copy password to clipboard

In case a password is saved with your GPG identity, it will be prompted through a modal window.

### Filter

Currently password filter is only done on the password name, not on the folder name.

A future enhancement will provide a better filter functionnality.

`ppass <command> <anything>` will filter displayed passwords based on `anything` value (name containing this value).

### Add a new store

You can create several stores (config sections). Default store path is `${HOME}/.ppass-${NAME}/`

```bash
ppass -c "${STORE}" init --new-section
```

You can also select path via the option `--path`. The folder will be created if it does not exist.

```bash
ppass -c "${STORE}" init --new-section --path "${PATH}"
```

### Use a store

All functions can be used for a specific store by using the `-c` option from **ppass** application.

```bash
ppass -c "${STORE}" generate ...
ppass -c "${STORE}" insert ...
ppass -c "${STORE}" open ...
ppass -c "${STORE}" clip ...
# etc.
```

### Initialise new git repository

You can initialise a new git repository in store path. It will set automatic git push for every password creation or modification. The git repository needs to be created on your platform before.

A default branch `main` is created.

```bash
ppass -c "${STORE}" init-git
```

You can also pass parameter through cli command:

```bash
ppass -c "${STORE}" init-git --repo "${REPO}" --user "${USER}" --mail "${EMAIL}"
```

### Initialise from existing git repository

If the git repository already exists, you can restore it in the current store folder by adding the `--pull` option to `init-git` command.

It will download the latest commit from `main` branch. If the branch name is different, you can update it in the config file through `ppass init --edit`.

### Publish to git

When a git repository is enabled, all changes to passwords will be pushed to remote. However, there will never be automatic pull to retrieve potential password changes from remote (from other application, computer, user, android app, aso.).

Automatic pull is not activated so that access to password remain fast.

It can be done manually through

```bash
ppass -c "${STORE} git pull"
  # or
ppass -c "${STORE} git sync" # pull then push
```

In case a remote change is done but not pulled, the automatic push on password modification will fail. A manual `git sync` will be required to merge local and remote.

### Change output to JSON

Default application prints in the cli items in a user friendly way: tables, prompts, aso.

It is however possible to pass all required parameters through command options, and retrieve function results in JSON format.

```bash
ppass --json <command> ...
```

### Shortcuts and Aliases

Application must give a fast access to passwords to be useful.

All commands can be called by shortcuts with their first letter(s):
* `g` for `generate`
* `c` for `clip`
* `o` for `open`
* ...

I personnaly also defined shortcuts in my home `.bashrc` file:

```bash
alias pp='ppass -c PRO'
alias ppc='ppass -c PRO clip'
alias ppo='ppass -c PRO open'
alias ppp='ppass -c PERSO'
alias pppc='ppass -c PERSO clip'
alias pppo='ppass -c PERSO open'
```

## SSH Connexion

In case you are using login / password to connect to a server through SSH, it can be done via **ppass**. Please note that we discourage such type of connexion. Prefer a connexion with [SSH keys](https://www.ssh.com/academy/ssh/key) instead.

In **ppass**, set `"ssh+${DOMAIN}"` in the url field.

The `open` and `clip` commands will open a new terminal and fill in SSH connexion.

Please note this is using `gnome-terminal` as an additional application dependency.


## Build

**Requirements**

- debhelper: `sudo apt install debhelper`
- [dh-virtualenv](https://github.com/spotify/dh-virtualenv)
- [build](https://github.com/pypa/build)
- [virtualenv](https://virtualenv.pypa.io/en/latest/)

**Commands**

```bash
poetry install

# build deb
dpkg-buildpackage -us -uc
dpkg-buildpackage -Tclean

# build python package
python3 -m build
```

## Dependencies

**Python Libraries**
- [click](https://palletsprojects.com/p/click/)
- [rich](https://github.com/Textualize/rich)
- [pyclip](https://pypi.org/project/pyclip/)
- [python-gnupg](https://docs.red-dove.com/python-gnupg/)

**Python Development Libraries**
- [poetry](https://python-poetry.org/)

## Author

Sébastien Guerri - [github page](https://github.com/sguerri)

## Issues

Contributions, issues and feature requests are welcome!

Feel free to check [issues page](https://github.com/sguerri/ppass/issues). You can also contact me.

## License

Copyright (C) 2022 Sebastien Guerri

ppass is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or any later version.

ppass is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with ppass. If not, see <https://www.gnu.org/licenses/>.