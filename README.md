### Hexlet tests and linter status:
[![Actions Status](https://github.com/sudobooo/python-project-lvl3/workflows/hexlet-check/badge.svg)](https://github.com/sudobooo/python-project-lvl3/actions)
[![Python CI](https://github.com/sudobooo/python-project-lvl3/actions/workflows/pyci.yml/badge.svg)](https://github.com/sudobooo/python-project-lvl3/actions/workflows/pyci.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/8ccab16f0538b0691b1c/maintainability)](https://codeclimate.com/github/sudobooo/python-project-lvl3/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/8ccab16f0538b0691b1c/test_coverage)](https://codeclimate.com/github/sudobooo/python-project-lvl3/test_coverage)

# Page-loader

The third project written for the academic purposes of a Hexlet's course on learning a programming language Python.

## About the project

Page-loader is web page downloader.

- The page is downloaded in html format.
- Content is downloaded only that which is located on the same domain.
- Can be used as CLI tool or library

## How to install and use

### Install
`python3 -m pip install git+https://github.com/sudobooo/python-project-lvl3`

### Use as a library
```
from page_loader import download

path_to_page = download(url, actual_path=os.getcwd())
print(path_to_page)
```

### Use as a CLI
```
usage: page-loader [options] <url>

description: web page downloader

positional arguments:
  url

optional arguments:
  -h, --help            show this help message and exit
  -V, --version         output the version number
  -o [dir], --output [dir]
                        output dir (default: working directory)
```

### Logging

All error logs are written to .page-loader-errors.log.
The file is created in the working directory.

## Demonstration of the program

### Asciinema page download
[![asciicast](https://asciinema.org/a/498469.svg)](https://asciinema.org/a/498469)

### Asciinema logging page-loader
[![asciicast](https://asciinema.org/a/498470.svg)](https://asciinema.org/a/498470)
