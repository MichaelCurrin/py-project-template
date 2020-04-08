"""
Sample python script.

This is a reference for laying out a Python script and be deleted.

It contains the following, layed out according to PEP-8 naming and spacing:
- imports
- global variables
- functions
- main function
- call to main function, using command-line arguments and ignoring the path to the
    file itself at index 0.
"""
# pylint: disable=blacklisted-name,invalid-name
import sys


SOME_GLOBAL = "My global"


def foo():
    """
    Foo docstring here.
    """
    return


def bar(a, b):
    """
    Bar docstring here.
    """
    return a + b


def main(args):
    """
    Main command-line function.
    """
    print("It works!")
    print("Args:")
    print(args)
    print(SOME_GLOBAL)

    foo()
    x = bar(1, 2)
    print(x)


if __name__ == "__main__":
    main(sys.argv[1:])
