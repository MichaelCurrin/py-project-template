# Python Project Template 🐍 📦
> Starter template for a Python app - including CI and docs

<!-- Shields generated with https://michaelcurrin.github.io/badge-generator/ -->

[![Python CI](https://github.com/MichaelCurrin/py-project-template/actions/workflows/main.yml/badge.svg)](https://github.com/MichaelCurrin/py-project-template/actions/workflows/main.yml)
[![GitHub tag](https://img.shields.io/github/tag/MichaelCurrin/py-project-template?include_prereleases=&sort=semver)](https://github.com/MichaelCurrin/py-project-template/releases/)
[![License](https://img.shields.io/badge/License-MIT-blue)](#license)

[![Made with Python](https://img.shields.io/badge/Python->=3.6-blue?logo=python&logoColor=white)](https://python.org "Go to Python website")

<!-- You can take these out if you don't care about them in your new project. -->
[![code style - black](https://img.shields.io/badge/code_style-black-blue)](https://black.readthedocs.io/)
[![dev dependency - flake8](https://img.shields.io/badge/dev_dependency-flake8-blue)](https://pypi.org/project/flake8)
[![dev dependency - pylint](https://img.shields.io/badge/dev_dependency-pylint-blue)](https://pypi.org/project/pylint)
[![dev dependency - mypy](https://img.shields.io/badge/dev_dependency-mypy-blue)](https://pypi.org/project/mypy)
[![dev dependency - pytest](https://img.shields.io/badge/dev_dependency-pytest-blue)](https://pypi.org/project/pytest)

## Purpose

This project provides a template for a Python application, enabling you to get up and running fast with local development and then move quickly when you want deploy your app to the cloud with confidence.

It includes a solid setup, from installing packages to running code quality checks locally and with GitHub Actions.

What you get:

- [x] Generic Python app code in [pyproject](/pyproject/), with sample tests in [tests](/tests/).
- [x] Sample documentation.
- [x] [Makefile](/Makefile) for running `make` commands (for macOS and Linux).
- [x] Requirements files for prod packages and dev packages, installed with `pip` using `make` commands.
- [x] Code quality checks - `flake8`, `pylint`, `mypy` (type checking), and `pytest`, including `make` commands and configs for each.
- [x] Git push hooks, to run checks on pushing.
- [x] GitHub Actions pipeline config.
- [x] Configs - VS Code, EditorConfig, and a Git ignore file.


## How to use this starter project

Create your own repo from this one:

<div align="center">

[![Use this template](https://img.shields.io/badge/Generate-Use_this_template-2ea44f?style=for-the-badge)](https://github.com/MichaelCurrin/py-project-template/generate)

</div>

See the [Template Notes](/docs/template-notes/) part of the docs for more info on how to use this template. And for links to my other templates.


## Sample usage

_TODO: Add just a few lines to show how to use your application. Such as a Python or shell snippet._

```sh
$ foo-bar --help
```

```sh
$ make install
$ make run
```


```python
import foo

foo.bar(123)
```



## Documentation
> How to install and run this project

<div align="center">

[![view - Documentation](https://img.shields.io/badge/view-Documentation-blue?style=for-the-badge)](https://michaelcurrin.github.io/py-project-template/)

</div>


## License

Released under [MIT](/LICENSE) by [@MichaelCurrin](https://github.com/MichaelCurrin).

A copy of the original license must be included if a significant portion of this template or project is used. You could rename it to `LICENSE-source` and then include your own `LICENSE` file with your name.
