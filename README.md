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

Stores created with **ppass** are 100% compatible with **[pass](https://www.passwordstore.org/)**. They are thus also compatible with pass clients like [Android Password Store](https://github.com/android-password-store/Android-Password-Store#readme).


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

The application is developped and used on debian 10 and ubuntu 21.10. Any feedback on other platforms is welcomed.

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

### Install from deb package

A deb package is available, built using `dh-virtualenv`. Installing this package will create a new Python virtual environment in `opt/venvs`. It will then create the symlink `usr/bin/ppass` pointing to `opt/venvs/ppass/bin/ppass`.

Download latest `.deb` file from the [release page](https://github.com/sguerri/ppass/releases).

```bash
sudo dpkg -i ppass_0.1.7_amd64.deb
```

### Install from ppa

The deb file is also available in my ppa.

<mark>TO CONFIRM
add-apt-repository ppa:s.noack/ppa
???
</mark>
```bash
curl -s --compressed "https://sguerri.github.io/ppa/KEY.gpg" | sudo apt-key add -
sudo curl -s --compressed -o /etc/apt/sources.list.d/pmp.list "https://sguerri.github.io/ppa/dists/files.list"
sudo apt update
sudo apt install pmppmp
```

## Usage

### Initialise

**ppass** creates a configuration file `.ppassrc` in the user home directory.



### Initialise from git

### Publish to git

### Add a new config section

### Manage folders

### Manage password files

### Create a new password

### Clip username and password

### Change output to JSON

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

Sébastien Guerri - <nierrgu@bmel.fr> - [github page](https://github.com/sguerri)

## Issues

Contributions, issues and feature requests are welcome!

Feel free to check [issues page](https://github.com/sguerri/ppass/issues). You can also contact me.

## License

Copyright (C) 2022 Sebastien Guerri

ppass is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or any later version.

ppass is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with ppass. If not, see <https://www.gnu.org/licenses/>.