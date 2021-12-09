"""
HTML Screenshot application.
"""
import sys

from . import download, lib, scrape

def is_binary_data(url) -> bool:
    """
    Determine whether the URL is for a page of plain HTML or binary data.
    """
    url = url.lower()
    
    return url.endswith(".pdf") or url.endswith(".png") or url.endswith(".jpeg") or url.endswith(".jpg")


def process(path_str: str) -> None:
    """
    Scrape all URLs for given text file path.
    """
    urls = lib.read(path_str)

    print(f"Found URLs: {len(urls)}")

    scrape.setup_driver()

    errors = []

    for url in urls:
        try:
            if is_binary_data(url):
                download.download_binary(url)
            else:
                scrape.process(url, fullpage=True)
        except Exception as e:
            errors.append(f"{url} - {str(e)}")

    scrape.close()

    if errors:
        for msg in errors:
            print(msg)
        print()

        sys.exit(1)


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
