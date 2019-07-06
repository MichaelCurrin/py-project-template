"""
Main application file.

This should be named after the project (or as shorter version), with no hyphens
or underscores. This could be named main.py instead.

If this is named __main__.py, then python will allow you to do the following:
$ python pyprojecttemplate/
...

Note that even if __main__.py is an executable, you cannot execute its
containing directory as you'll get an error.
"""
### Imports ###
import sys


### Globals constants ###

SOME_GLOBAL = "My global"

### Functions ###

def main(args):
    """
    Main command-line function.
    """
    print("It works!")
    print("Args:")
    print(args)
    print(SOME_GLOBAL)


if __name__ == '__main__':
    main(sys.argv[1:])
