# HTML Screenshot PY
> Python web scraper that creates screenshot images for given URLs

A simple CLI app to automate taking screenshots of websites, whether your own or by others.

Based on [Tutorial](https://pythonbasics.org/selenium-screenshot/).


## Sample

```sh
$ python -m htmlscreenshot.scrape 'https://example.com'
```

Then find your PNG in the project's output directory.


## Installation

### Requirements

- [Python 3](https://www.python.org)
- Firefox
- [Geckodriver](https://firefox-source-docs.mozilla.org/testing/geckodriver/index.html)

### Install system dependencies

- [Install Python 3](https://gist.github.com/MichaelCurrin/57caae30bd7b0991098e9804a9494c23)
- [Install Firefox](https://www.mozilla.org/en-US/firefox/new/)
- [Install Geckodriver](https://gist.github.com/MichaelCurrin/877a6ab95d6e8edcd1b1bcb60e71815f)

### Clone

```sh
$ git clone git@github.com:MichaelCurrin/html-screenshot-py.git
$ cd html-screenshot-py
```

### Install project packages

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


## Usage

Generated screenshots will be in the unversioned `htmlscreenshot/var/` directory.

### Help

View CLI help.

```sh
$ make page-help
```

```sh
$ make pages-help
```

### Demo

Run one of the demo tasks.

```sh
$ make page-demo
```

This uses URLs in the [sample.txt](/htmlscreenshot/sample.txt) file.

```sh
$ make pages-demo
```

### Run

Run against a single URL. e.g.

```sh
$ python -m htmlscreenshot.scrape 'https://example.com'
```

Run against a text file of URLs. e.g.

```sh
$ python -m htmlscreenshot ~/path/to/urls.txt
```

Where the file is one URL per like, like [sample.txt](/htmlscreenshot/sample.txt).


## License

MIT
