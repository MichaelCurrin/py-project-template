"""
Download module.

Handle fetching and saving of binary data. This uses the traditional `requests`
package, without any browser.
"""
import sys
from pathlib import Path

import requests

from . import lib
from .lib import ADD_DATETIME_DEFAULT, PDF_DIR


EXT = ".pdf"


def fetch(url: str) -> bytes:
    """
    Request a page URL and get the response content in bytes.

    The stream param is not strictly needed to handle a PDF as it works without
    it, but it was recommended in a thread. The param sets a header so that
    response comes in chunks.

    :raises: HTTPError for 4xx or 5xx response.
    """
    resp = requests.get(url, stream=True)

    resp.raise_for_status()

    return resp.content


def write_binary(path: Path, content: bytes) -> None:
    """
    Write given binary data to a file.

    e.g. Write a PDF file.
    """
    with open(path, "wb") as f_out:
        f_out.write(content)


def download_binary(url: str) -> None:
    """
    Fetch and download binary data at URL.
    """
    print(f"Downloading binary content: {url}")
    content = fetch(url)

    slug_filename = lib.make_filename(url, EXT, ADD_DATETIME_DEFAULT)
    out_path = PDF_DIR / slug_filename

    write_binary(out_path, content)


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
