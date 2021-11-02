# HTML Screenshot PY 🌐 🖼 🐍
> CLI tool to take screenshots of given webpages

[![Made with Python](https://img.shields.io/badge/Python->=3.6-blue?logo=python&logoColor=white)](https://python.org)
[![dependency - selenium](https://img.shields.io/badge/selenium-3-blue)](https://pypi.org/project/selenium)

The web is fast-changing - maybe you want to save an article or a design that inspires you before it moves or disappears from the internet. Or maybe you want to track the changes to a website over time.

Now you can use this easy Python CLI tool. Provide your URLs for webpages to scrape, whether for your own sites or by someone else. The tool will go through each to load the page and store as a PNG file.


## Sample

One webpage:

```sh
$ python -m htmlscreenshot.scrape 'https://example.com'
```

Multiple URLs:

```sh
$ python -m htmlscreenshot ~/path/to/urls.txt
```

Then find your PNGs in the project's output directory.


## Documentation

<div align="center">

[![view - Documentation](https://img.shields.io/badge/view-Online_Documentation-blue?style=for-the-badge)](https://michaelcurrin.github.io/html-screenshot-py/ "Go to docs site")

</div>


## License

Released under [MIT](/LICENSE) by [@MichaelCurrin](https://github.com/MichaelCurrin).
