
# Usage

Generated screenshots will be in the unversioned `htmlscreenshot/var/` directory.


## Help

View CLI help.

```sh
$ make page-help
```

```sh
$ make pages-help
```


## Demo

Run demo tasks against some fixed URLs that have been configured.

Screenshot one page.

```sh
$ make page-demo
```

Screenshot each page listed in the [sample.txt](/htmlscreenshot/sample.txt) file.

```sh
$ make pages-demo
```

See images here created:

```console
$ ls -1 htmlscreenshot/var
Michael-Currin.png
Twitter-It-s-what-s-happening-Twitter.png
Welcome-to-Python-org.png
```


## Run

Screenshot against a single URL using the `scrape` module. e.g.

```sh
$ python -m htmlscreenshot.scrape 'https://example.com'
```

Screenshot against a text file of URLs using the main module e.g.

```sh
$ python -m htmlscreenshot ~/path/to/urls.txt
```

Where the file is one URL per like, like [sample.txt](/htmlscreenshot/sample.txt).
