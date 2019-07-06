# Py Project Template
> Python 3 project scaffolding - covers directory structure, scripts and docs

The style is based on conventions in the Python community, what I have picked up from other developers I have worked with, plus some of my own preferences which I've evolved over time.

This repo is a good starting point for new projects plus I can use it as a reference of existing projects where I want a base structure reminder, or I need to copy a text fragment which is very reusable with a bit of tweaking.

## Naming conventions

This section explains the naming of directories this project

Unix has a convention of naming the root user's directories. Here are some which are relevant for this project:

- `/bin` - Binary executables. Essential commands that need to be available for all users.
- `/etc` - System-wide configuration files.
- `/lib` - Libraries need for binaries in `/bin`.
- `/var` - Variable files, such as logs.

Read more about those [here](https://github.com/MichaelCurrin/learn-to-code/blob/master/Bash/beginning_linux_programming/directory_structure.md)

That naming style has been adopted for naming of directories within this project. That might seem might seem quirky, as I picked this up as a style from somewhere I worked before and haven't seen it in other projects. However, it makes sense to me and therefore I've adopted it for my own projects.

Recommendations for using the project's directories (paths given relative to repo root):

- [/bin/](/bin/) - Executable files. Usually a bash script, such as to run a python script within an environment, run a curl command or pipe data in or out of sqlite.
- [/pyprojecttemplate/](/pyprojecttemplate/) - Main application scripts such as a server or command-line scripts should live in the top project directory, in this case named `pyprojecttemplate`. These should preferably not import from each other but can import from the `lib` module.
- [/pyprojecttemplate/lib/](/pyprojecttemplate/lib/) - Library of common scripts. These should be independent of each other (i.e. do not import from each other), to reduce circular dependencies. They should also not depend on an `__init__.py` script. Any common logic such as setting up a path to the app directory should be setup in the `__init__.py` script.
- [/pyprojecttemplate/etc/](/pyprojecttemplate/etc/) - Configuration files. For files such as `.json`, `.yml`, `.ini` or `.conf`.
- [/pyprojecttemplate/utils/](/pyprojecttemplate/utils/) - Utilities. Standalone scripts which may use the `lib` module. These `utils` scripts should also be independent from each other should. If you find when developing that there is any logic duplicated across `utils` scripts, then that should be moved to a `lib` script and imported from `lib` into `utils` scripts.
- [pyprojecttemplate/var/](pyprojecttemplate/var/) - Variable content such as a database file or text/CSV/JSON files to be used for input or which are outputted by a script. No scripts should live in the this directory.

Benefits I found of this approach:

- I find the logical grouping makes makes writing and finding code easier. e.g. If a script is intended as a library, it goes in `lib` with similar scripts.
- It means that it is easy to switch between my projects as the layout is familiar.
- Imports are easier
    * Imports are easy to think about and trace. You can see the role of a script based on what module it is in.
    * Scripts are more independent and therefore more robust.
    * It's easier to avoid circular imports and complicated imports (e.g. where a script uses a script uses script in a deep or haphazard structure).
