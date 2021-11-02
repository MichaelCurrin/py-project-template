# Installation


## Requirements

- [Make](https://www.gnu.org/software/make/) - standard on Linux and macOS. Install on Windows or use the commands in Makefile without `make`.
- [Python 3](https://www.python.org)
- Firefox
- [Geckodriver](https://firefox-source-docs.mozilla.org/testing/geckodriver/index.html)


## Install system dependencies

- [Install Python 3](https://gist.github.com/MichaelCurrin/57caae30bd7b0991098e9804a9494c23)
- [Install Firefox](https://www.mozilla.org/en-US/firefox/new/)
- [Install Geckodriver](https://gist.github.com/MichaelCurrin/877a6ab95d6e8edcd1b1bcb60e71815f)


## Clone

```sh
$ git clone git@github.com:MichaelCurrin/html-screenshot-py.git
$ cd html-screenshot-py
```


## Install project packages

Create a Python virtual environment.

```bash
$ python3 -m venv venv
$ source venv/bin/activate
```

Install packages into it.

```sh
$ make install
```

_Note use of Selenium 3, as version 4 causes Geckodriver to crash._
