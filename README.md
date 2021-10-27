# HTML Screenshot PY
> Python web scraper that creates screenshot images for given URLs

Based on [Tutorial](https://pythonbasics.org/selenium-screenshot/).

Note use of Selenium 3, as version 4 causes Geckodriver to crash.


## Requirements

- Python 3
- Firefox
- Geckodriver


## Installation

Install system dependencies:

- Python 3
- Firefox
- Geckodriver

Install project packages:

```sh
$ make install
```


## Usage

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
