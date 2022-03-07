# Welcome to ppass

[![](https://badgen.net/github/release/sguerri/ppass)](https://github.com/sguerri/ppass/releases/)
[![](https://img.shields.io/github/workflow/status/sguerri/ppass/build)](https://github.com/sguerri/ppass/actions/workflows/build.yml)
[![](https://badgen.net/github/license/sguerri/ppass)](https://www.gnu.org/licenses/)
[![](https://badgen.net/pypi/v/ppass)](https://pypi.org/project/ppass/)
![](https://badgen.net/pypi/python/ppass)
[![](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](#)

> GPG Password Manager

**ppass** is heavily inspired from **[pass](https://www.passwordstore.org/)**

I wanted to extend some of its functionnalities, and decided to rewrite the application in Python. It was a good exercice to try Python as I am more used to program in js/ts and c++/qt.

This beeing said, **ppass** is not as well tested or stable as **[pass](https://www.passwordstore.org/)**. I intend to make it evolve in the future, as I am using it on a daily basis. I am however alone on this one. If you want stability and portability, with a great community, please use **[pass](https://www.passwordstore.org/)**.

Stores created with **ppass** are compatible with **[pass](https://www.passwordstore.org/)**. They are thus also compatible with pass clients like [Android Password Store](https://github.com/android-password-store/Android-Password-Store#readme).


**Main features**
* gpg password creation (one file per password)
* enhanced password file with username, url and comments
* git integration
* possibility to handle several distinct stores
* open web browser from password file
* automatic fill in username and password to web browser
* cli user interface or json response

**Roadmap**
* autocompletion
* enhanced clip functionnality
* test on other platforms
* produce deb files (tested with dh-virtualenv but dependent python version)
* code cleaning
* more to come...

---

- [Welcome to ppass](#welcome-to-ppass)
  * [Installation](#installation)
  * [Usage](#usage)
    + [fdsfds](#fdsfds)
  * [Build](#build)
  * [Dependencies](#dependencies)
  * [Author](#author)
  * [Issues](#issues)
  * [License](#license)

## Installation

### Requirements

The application is developped and used on ubuntu 21.10, with python 3.9.7. Any feedback on other platforms is welcomed.

<mark>A VOIR xdotool + wayland</mark>

- python3 >=3.7,<4.0
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

ppass folders create --name "Name of folder"
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

<mark>TODO with enhanced filter</mark>

### Add a new store

You can create several stores (config sections).

```bash
ppass init --new-section
```

<mark>NE MARCHE PAS</mark>

ppass -c "PERSO" init --new-section --path "/home/sebastien/.ppass-perso"

### Initialise from git

### Publish to git




### Change output to JSON

### Shortcuts and Aliases



## Build

**Requirements**

- [build](https://github.com/pypa/build)

**Commands**

```bash
poetry install

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