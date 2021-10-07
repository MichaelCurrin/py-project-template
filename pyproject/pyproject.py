"""
Main application file.
"""
import sys

from . import foo
from .lib import greet


def main(args):
    """
    Main command-line function.
    """
    name = args.pop(0)
    print(greet(name))

    print(foo.greet(name))


if __name__ == "__main__":
    main(sys.argv[1:])
