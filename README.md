# Py Project Template
> Python 3 project scaffolding - covers directory structure, scripts and docs.

<!-- Shields from https://shields.io/ -->
[![Use this template](https://img.shields.io/badge/Use_this_template-brightgreen.svg)](https://github.com/MichaelCurrin/py-project-template/generate)
[![Actions status](https://github.com/MichaelCurrin/py-project-template/workflows/Python%20application/badge.svg)](https://github.com/MichaelCurrin/py-project-template/actions)
[![GitHub tag](https://img.shields.io/github/tag/MichaelCurrin/py-project-template.svg)](https://GitHub.com/MichaelCurrin/py-project-template/tags/)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/MichaelCurrin/py-project-template/blob/master/LICENSE)

The style is based on conventions in the Python community, what I have picked up from other developers I have worked with, plus some of my own preferences which I've evolved over time.

This repo is a good starting point for new projects plus I can use it as a reference of existing projects where I want a base structure reminder, or I need to copy a text fragment which is very reusable with a bit of tweaking.

To use this project, follow either the [Add VS Code boilerplate](#add-vs-code-boilerplate) or [Use this base project](#use-this-base-project) sections. Keep reading later in the doc if you need more detail.

- [Add VS Code boilerplate](#add-vs-code-boilerplate)
- [Use this base project](#use-this-base-project)
    - [Get a local copy of the base project](#get-a-local-copy-of-the-base-project)
    - [Replace the README](#replace-the-readme)
    - [Complete project name references](#complete-project-name-references)
    - [Cleanup](#cleanup)
- [Explanations and notes](#explanations-and-notes)
    - [VSCode Settings](#vscode-settings)
        - [Settings](#settings)
        - [Launch](#launch)
        - [Dotenv](#dotenv)
- [Naming conventions](#naming-conventions)
- [Git Ignore](#git-ignore)
    - [Data files](#data-files)
- [Badges](#badges)
    - [Rules for static text badges](#rules-for-static-text-badges)
    - [Examples](#examples)
    - [Placement](#placement)
- [Repo admin](#repo-admin)
    - [Formatting](#formatting)


## Add VS Code boilerplate

Follow this section to improve code linting and code running in VS Code. This copies files from Github straight to your repo. No cloning needed.

- **settings** - Starts your terminal in the app directory. Ensures that the Python link in your virtual environment is used throughout the IDE - in particular this ensures that linting picks up imports from your virtual environment.
- **launch** - When you click run button within _Debug_ panel, you run debugger within the virtual environment. Note that if you read/write a file in the script, the path should be relative to the project root directory for the debugger to work, not the app directory, even if the script and text file are both in the app directory. FIXME: See if this can be fixed with a launch config change.
- **dotenv**: Starts your terminal with Python virtual environment activated (provided you have the VS Code _Python_ extension running).

(Despite these settings, the Run button in the top right of the IDE does not start in a virtual environment unfortunately. That's okay as Debug can also run but is more powerful.)

```bash
$ cd <PATH_TO_YOUR_PROJECT>
```

Then run the following in your terminal to copy the scripts from Github in your project. _WARNING: This it will overwrite any existing files._

```bash
mkdir -p .vscode
BASE_URL='https://raw.githubusercontent.com/MichaelCurrin/py-project-template/master'
curl "$BASE_URL/.vscode/settings.json" > .vscode/settings.json
curl "$BASE_URL/.vscode/launch.json" > .vscode/launch.json
curl "$BASE_URL/.env" > .env
```

Edit the local files and complete the _TODO_ items in them.


## Use this base project

Follow this section fo instructions on how to copy of this entire repo as a base project and then customize it.

### Get a local copy of the base project

1. Click [Use this template](https://github.com/MichaelCurrin/py-project-template/generate) to create a new project started from this repo.
2. Create a local clone of your repo.
3. Navigate to your repo directory.


### Replace the README

Note the force flag to overwrite.

```bash
$ giv mv -f README.template.md README.md
```

Then customize the new `README.md` as you like.


### Complete project name references

Rename the Python project directory and script to your custom name. For example: `myprojectname`.

```bash
$ cd <PATH_TO_REPO>
$ git mv pyprojectemplate myprojectname
$ cd myprojectname
```

Setup main application file.

```bash
$ git rm pyprojectemplate.py
$ touch myprojectname.py  # Replace with your own projectname.
```

Go through the _TODO_ items in the repo and complete them. See the rest is README if you don't know what a file is for.

_FIXME: Is there is a way to use find, grep etc. to replace mentions across all files without going detailed? And on directory name. Also note renaming local repo folder._


### Cleanup

If you don't need directories in project directory, delete them. They contain `.gitkeep` files - once deleted those changes must be added to version control.

Delete [LICENSE](/LICENSE) and replace with your own.


## Explanations and notes

### VSCode Settings

Ignore/delete if you don't use [Visual Studio Code](https://code.visualstudio.com/).

See the [.vscode](/.vscode) directory.

The _settings_ file helps with running code and adding a gutter at 79 characters. The _launch_ file can be used with the debug panel to run a Python script which is open in the IDE.

#### Settings

The `python.pythonPath` value for User settings defaults to `"python"`.

If you use a virtual environment, use the _venv_ path in the settings file. This must be the full path - it will not pickup correctly inside the _venv_ if left as `"python"`.

If you don't use a virtual environment, the User default could be fine. You could override it in the User or Workspace level to one of the following:

- `python3`
- `/usr/bin/python3`
- `/usr/bin/python3.X` - e.g. `3.6`. If you use the VSCode GUI to select the environment it might look like this.

If you set config values in a dotenv file, you might want to add this to your settings file:

```
    "python.envFile": "${workspaceFolder}/.env"
```

#### Launch

The [launch.json](/.vscode/launch.json) file contains configurations for scripts or commands which can be run from the Debug panel, using the droplist and play button.

This configuration can be left as is or you can add to it.

The config already contains an item to run a Python script in the terminal, if it open and in view in the IDE.

If you find yourself regularly running particular Python scripts or modules and want to do so without having to first open the script, then add an item for that specific script.

#### Dotenv

This template comes with a _dotenv_ file - [.env](/.env) which includes paths to import from, including the project directory and the virtual environment. Having that there helps with running or linting files in an IDE such as VSCode.

For interest, the file works in VSCode because of this global config setting:

```
"python.envFile": "${workspaceFolder}/.env"
```

## Naming conventions

This section explains the naming of directories this project

Unix has a convention of naming the root user's directories. Here are some which are relevant for this project:

- `/bin` - Binary executables. Essential commands that need to be available for all users.
- `/etc` - System-wide configuration files.
- `/lib` - Libraries need for binaries in `/bin`.
- `/var` - Variable files, such as logs.

Read more about those [here](https://github.com/MichaelCurrin/learn-to-code/blob/master/Bash/beginning_linux_programming/directory_structure.md).

That naming style has been adopted for naming of directories within this project. That might seem might seem quirky, as I picked this up as a style from somewhere I worked before and haven't seen it in other projects. However, it makes sense to me and therefore I've adopted it for my own projects.

Recommendations for using the project's directories (paths given relative to repo root):

- **[/bin/](/bin/)** - Executable files. Usually a bash script, such as to run a python script within an environment, run a curl command or pipe data in or out of sqlite.
- **[/pyprojecttemplate/](/pyprojecttemplate/)** - Main application scripts such as a server or command-line scripts should live in the top project directory, in this case named `pyprojecttemplate`. These should preferably not import from each other but can import from the `lib` module.
- **[/pyprojecttemplate/lib/](/pyprojecttemplate/lib/)** - Library of common scripts. These should be independent of each other (i.e. do not import from each other), to reduce circular dependencies. They should also not depend on an `__init__.py` script. Any common logic such as setting up a path to the app directory should be setup in the `__init__.py` script.
- **[/pyprojecttemplate/etc/](/pyprojecttemplate/etc/)** - Configuration files. For files such as `.json`, `.yml`, `.ini` or `.conf`.
- **[/pyprojecttemplate/utils/](/pyprojecttemplate/utils/)** - Utilities. Standalone scripts which may use the `lib` module. These `utils` scripts should also be independent from each other should. If you find when developing that there is any logic duplicated across `utils` scripts, then that should be moved to a `lib` script and imported from `lib` into `utils` scripts.
- **[/pyprojecttemplate/var/](/pyprojecttemplate/var/)** - Variable content such as a database file or text/CSV/JSON files to be used for input or which are outputted by a script. No scripts should live in the this directory.

Benefits I found of this approach:

- I find the logical grouping makes makes writing and finding code easier. e.g. If a script is intended as a library, it goes in `lib` with similar scripts.
- It means that it is easy to switch between my projects as the layout is familiar.
- Imports are easier
    * Imports are easy to think about and trace. You can see the role of a script based on what module it is in.
    * Scripts are more independent and therefore more robust.
    * It's easier to avoid circular imports and complicated imports (e.g. where a script uses a script uses script in a deep or haphazard structure).


## Git Ignore

Optional additions for [.gitignore](/.gitignore).


### Data files

Ignore files of a certain type project-wide. e.g. `.csv`, `.json`.

```
# Local CSVs and their lock files (if they are open in an editor).
*.csv
*.~lock.*.csv#
```

Do this project-wide at the risk that you will have unversioned CSVs left all over your project which do not show up using `git status`. Also, in some cases you may want to version as CSV or JSON file and you will have to use `git add -f FILE` to add it.

Or ignore CSV files in specific paths such as project variable files directory. The rule could be:

```
# Local CSVs and their lock files (if they are open in an editor).
pyprojecttemplate/var/*.csv
pyprojecttemplate/var/.~lock.*.csv#
```

## Badges

The badges for this project's docs are sourced from [naereen.github.io/badges/](https://naereen.github.io/badges/).

Some of the badges have dynamic logic, for example they show the latest release number or whether a website is online or not. Others are hardcoded, but very flexible. You can use the samples in that resource above or create your own using this.

See the official [shields](https://shields.io/) site which includes instructions and a tool to make custom widgets.

Continue below to see my own recommendations based on limited experimentation.

### Rules for static text badges

- URL for badge image: `https://img.shields.io/badge/FILENAME`
- Format of filename to append to URL: `<SUBJECT>-<STATUS>-<COLOR>.svg`.
- The subject is used for status section (text in grey area).
- Status is used for status section (text in colored button area). Omit subject to only status button.
- Color defaults to green. Set a color using ANSI colors. e.g. `blue`, `green`, `cyan`. They can be more specific as hex values e.g. `0000ff`, `1f425f`.
- Use hyphens separating values as above, and an underscore or `%20` _within_ values to separate words.

### Examples

The filename `Coolness-Very_Awesome-purple.svg` displays:

[![Generic badge](https://img.shields.io/badge/Coolness%20Factor-Very_Awesome-purple.svg)](https://shields.io/)

Badge with description and image.

```
![Generic badge](https://img.shields.io/badge/Coolness%20Factor-Very_Awesome-purple.svg)
```

Add a clickable link to the badge.

```
[![Generic badge](https://img.shields.io/badge/Coolness%20Factor-Very_Awesome-purple.svg)](https://shields.io/)
```

General format for a clickable badge with static text.

```
[![Alt text description](https://img.shields.io/badge/<FILENAME>)](https://<OUT_BOUND_LINK>)
```

### Placement

To show badges side by side, separate them with spaces.

To lay them out them vertically, put them one line under each other. No blank line is needed. Note that normally markdown normally needs an empty line between sentences to create a line break, but that does not apply here. Except placing the badge on a newline directly below a sentence will still output as all one line.


## Repo admin

### Formatting

As an alternative to Black, you can use AutoPEP8 to format.

1. Replace `black` with `autopep8` in [requirements-dev.txt](/requirements-dev.txt).
2. Uninstall with
    ```sh
    $ pip uninstall autopep8
    ```
3. Install with
    ```sh
    $ make dev-install
    ```
4. Remove/update the format commands to use `autopep8` instead. e.g.
    ```
    fmt:
	    autopep8 --in-place --recursive pyprojecttemplate/

    fmt-diff:
	    autopep8 --diff --recursive pyprojecttemplate/
    ```
