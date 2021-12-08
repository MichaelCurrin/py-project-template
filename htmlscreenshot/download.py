import sys

import requests

from . import lib
from .lib import ADD_DATETIME_DEFAULT, OUT_DIR


def fetch(url):
    resp = requests.get(url, stream=True)

    return resp.content


def download_binary(url):
    print(url)
    content = fetch(url)

    out_name = lib.make_filename(url, ".pdf", ADD_DATETIME_DEFAULT)
    lib.write(OUT_DIR / out_name, content)


def main(args: list[str]) -> None:
    """
    Command-line entry-point.
    """
    if not args:
        print("Required arg: URL")
        sys.exit(0)

    url = args.pop(0)

    download_binary(url)


if __name__ == "__main__":
    main(sys.argv[1:])
