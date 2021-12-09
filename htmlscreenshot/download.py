"""
Download module.

Handle fetching and saving of binary data. This uses the traditional `requests`
package, without any browser.
"""
import sys

import requests

from . import lib
from .lib import ADD_DATETIME_DEFAULT, PNG_DIR


def fetch(url):
    """
    Get content of URL.

    The stream param is not strictly needed to handle a PDF or similar binary
    files, as it works without it, but it was recommended in a thread as is
    kept, possibly for performance.
    """
    resp = requests.get(url, stream=True)

    return resp.content


def download_binary(url: str) -> None:
    """
    Fetch and download binary data at URL.
    """
    print(f"Downloading: {url}")
    content = fetch(url)

    out_name = lib.make_filename(url, ".pdf", ADD_DATETIME_DEFAULT)
    out_path = PNG_DIR / out_name

    lib.write(out_path, content)


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
