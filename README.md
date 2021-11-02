# HTML Screenshot PY
> CLI tool to take screenshots of batches of URLs

[![Made with Python](https://img.shields.io/badge/Python->=3.6-blue?logo=python&logoColor=white)](https://python.org)
[![dependency - selenium](https://img.shields.io/badge/selenium-3-blue)](https://pypi.org/project/selenium)

A simple CLI app to make it easy to take screenshots of one or many webpages. Whether your own sites or by others.

The web is fast-changing - maybe you want to save an article or a design that inspires you before it moves or disappears from the internet. Or maybe you want to track the changes to a website over time.


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

[![view - Documentation](https://img.shields.io/badge/view-Documentation-blue?style=for-the-badge)](/docs/)

</div>


## License

Released under [MIT](/LICENSE) by [@MichaelCurrin](https://github.com/MichaelCurrin).
