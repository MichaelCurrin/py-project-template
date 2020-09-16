# Installation

_TODO: Delete any sections not needed._


## Project requirements

_TODO: Update for appropriate minimum Python version and any other OS or project-level packages covered later. Optionally add more links._

- some-os-package
- [Python](https://www.python.org/) >= 3.6
- some-py-package

_OR use a table_

| Name                                     | Description        |
| ---------------------------------------- | ------------------ |
| some-os-package                          | Some description.  |
| [Python](https://www.python.org/) >= 3.6 | Info about Python. |
| some-py-package                          | Some description.  |


## Install system dependencies

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

Inside a Python packages inside the project's virtual environment using steps below.

### Core dependencies

```sh
$ make install
```

You may continue to [Usage](/docs/usage.md) doc.

### Dev dependencies

Optionally install dev dependencies.

```sh
$ make install-dev
```
