# Welcome to pmp

[![](https://badgen.net/github/release/sguerri/pmp)](https://github.com/sguerri/pmp/releases/)
[![](https://img.shields.io/github/workflow/status/sguerri/pmp/build)](https://github.com/sguerri/pmp/actions/workflows/build.yml)
[![](https://badgen.net/github/license/sguerri/pmp)](https://www.gnu.org/licenses/)
[![](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](#)

<mark>lien pypi</mark>
[![](https://badgen.net/pypi/v/pmp)](https://pypi.org/project/pmp/)
![](https://badgen.net/pypi/python/pmp)

> GPG Password Manager




opt/venvs/pmp/bin/ppass usr/bin/ppass




<mark>TODO general comments</mark>

- [Welcome to pmp](#welcome-to-pmp)
  * [Installation](#installation)
  * [Usage](#usage)
    + [fdsfds](#fdsfds)
  * [Limitations](#limitations)
  * [Roadmap](#roadmap)
  * [Build](#build)
  * [Dependencies](#dependencies)
  * [Author](#author)
  * [Issues](#issues)
  * [License](#license)

## Getting started

<mark>
compatibility mpass
compatibility android app
</mark>

## Installation

### Requirements

<mark>Tested on linux debian</mark>

- python3 >=3.7,<4.0
- xdotool: `sudo apt install xdotool`
- git: `sudo apt install git`
- gpg: `sudo apt install gnupg`
- nano: `sudo apt install nano`
- xclip: `sudo apt install xclip`

### Install from pypi <mark>(pip, pipenv etc.)</mark>

The package is published on pypi <mark>LINK</mark>

```bash
pip install pmp
```

### Install from deb package

Download latest `.deb` file from the release section

```bash
sudo dpkg -i pmp_0.0.2_amd64.deb
```

### Install from ppa

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

Go to [https://sguerri.github.io/p5ball/index.html](https://sguerri.github.io/p5ball/index.html)

### Initialise

### Initialise from git

### Publish to git

### Add a new config section

### Manage folders

### Manage password files

### Create a new password

### Clip username and password

### Change output to JSON

## Limitations

<mark>TODO</mark>

## Roadmap

<mark>TODO</mark>

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

Sébastien Guerri - [Github](https://github.com/sguerri)

## Issues

Contributions, issues and feature requests are welcome!

Feel free to check [issues page](https://github.com/sguerri/pmp/issues). You can also contact the author.

## License

Copyright (C) 2022 Sebastien Guerri

pmp is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or any later version.

pmp is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with pmp. If not, see <https://www.gnu.org/licenses/>.