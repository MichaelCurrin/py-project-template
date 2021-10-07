"""
Main application file.
"""
import sys

from .lib import greet


def main(args):
    """
    Main command-line function.
    """
    name = args.pop(0)
    print(greet(name))


if __name__ == "__main__":
    main(sys.argv[1:])
