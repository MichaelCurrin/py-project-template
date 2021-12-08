"""
HTML Screenshot application.
"""
import sys

from . import download, lib, scrape


def process(path_str: str) -> None:
    """
    Scrape all URLs for given text file path.
    """
    urls = lib.read(path_str)

    print(f"Found URLs: {len(urls)}")
    print(urls)

    scrape.setup_driver()

    try:
        for url in urls:
            if url.endswith(".pdf"):
                download.download_binary(url)
            else:
                scrape.process(url)
    finally:
        scrape.close()


def main(args: list[str]) -> None:
    """
    Command-line entry-point.
    """
    if not args:
        print("Required arg: PATH")
        print("Provide a path to a text file of one URL per line")
        sys.exit(0)

    path_str = args.pop(0)
    process(path_str)


if __name__ == "__main__":
    main(sys.argv[1:])
