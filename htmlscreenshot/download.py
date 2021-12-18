"""
Download module.

Handle fetching and saving of binary data. This uses the traditional `requests`
package, without any browser.
"""
import sys

import requests

from . import lib
from .lib import ADD_DATETIME_DEFAULT, PNG_DIR


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


def download_binary(url: str) -> None:
    """
    Fetch and download binary data at URL.
    """
    print(f"Downloading binary content: {url}")
    content = fetch(url)

    slug_filename = lib.make_filename(url, ".pdf", ADD_DATETIME_DEFAULT)
    out_path = PNG_DIR / slug_filename

    lib.write_binary(out_path, content)


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
