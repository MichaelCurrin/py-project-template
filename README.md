# HTML Screenshot PY 🌐 🖼 🐍
> CLI tool to take screenshots of given webpages

[![GitHub tag](https://img.shields.io/github/tag/MichaelCurrin/html-screenshot-py?include_prereleases=&sort=semver&color=blue)](https://github.com/MichaelCurrin/html-screenshot-py/releases/)
[![License](https://img.shields.io/badge/License-MIT-blue)](#license)

[![Made with Python](https://img.shields.io/badge/Python->=3.6-blue?logo=python&logoColor=white)](https://python.org)
[![dependency - selenium](https://img.shields.io/badge/selenium-3-blue)](https://pypi.org/project/selenium)
[![dependency - requests](https://img.shields.io/badge/requests-2-blue)](https://pypi.org/project/requests)


## About

An easy Python CLI tool. Provide your URLs for webpages to scrape, whether for your own sites or by someone else. 

It supports to formats:

- HTML pages - The tool will go through each to load the page, take a screenshot of the _entire_ page and save it a PNG file.
- PDF pages - For files ending in `.pdf`, the file will be downloaded as as `.pdf` file (for speed and reliability) instead of trying to take a screenshot (which could be massive for PDFs with many pages).

Use-cases:

- Archive - Save a once-off copy of an article or a page design that inspires you, before it moves or disappears from the internet.
- Software development - Create visual snapshots of your own website to track improvements and fixes. Or watch how a competitor's website changes. 


## Sample usage 

For one webpage:

```sh
$ python -m htmlscreenshot.scrape 'https://example.com'
```

For multiple pages:

```sh
$ python -m htmlscreenshot ~/path/to/urls.txt
```

Then find your screenshots as PNGs in the project's output directory.


## Documentation

<div align="center">

[![view - Documentation](https://img.shields.io/badge/view-Online_Documentation-blue?style=for-the-badge)](https://michaelcurrin.github.io/html-screenshot-py/ "Go to docs site")

</div>


## License

Released under [MIT](/LICENSE) by [@MichaelCurrin](https://github.com/MichaelCurrin).
