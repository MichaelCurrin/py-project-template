# Installation

_TODO: Delete any sections not needed._


## Project requirements

_TODO: Update for appropriate minimum Python version and any other packages covered later._

- some-package
- Python 3.6+

## Install OS-level dependencies

_TODO: Include any instructions or commands to install a package or application, other than Python. Example below._

### macOS

Install [brew](https://brew.sh/).

Install packages with `brew`.

```bash
$ brew install some-package
```

### Ubuntu/Debian

Install packages with `apt` if you have it, otherwise `apt-get` can be used instead.

```bash
$ sudo apt update
$ sudo apt install some-package
```


## Install project dependencies

It is usually best-practice in _Python_ projects to install into a sandboxed _virtual environment_, This will be locked to a specific Python version and contain only the _Python_ libraries that you install into it, so that your _Python_ projects do not get affected.

Follow this guide to [Setup a Python 3 Virtual Environment](https://gist.github.com/MichaelCurrin/3a4d14ba1763b4d6a1884f56a01412b7). That includes steps to upgrade or install _Python_.

You can then continue to the [Usage](/docs/usage.md) doc.
