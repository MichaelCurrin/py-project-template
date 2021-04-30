"""
Main application file.
"""
import sys


def main(args):
    """
    Main command-line function.
    """
    print("Hello, World!")
    print()

    print("Args:")
    print(args)


if __name__ == "__main__":
    main(sys.argv[1:])
