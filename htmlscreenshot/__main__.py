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

    return (
        url.endswith(".pdf")
        or url.endswith(".png")
        or url.endswith(".jpeg")
        or url.endswith(".jpg")
    )


def handle_errors(errors: list[str]) -> None:
    """
    Log errors if any.
    """
    if errors:
        print("\nERRORS")

        for i, error_msg in enumerate(errors):
            print(f"  - {i+1}. {error_msg}")

        sys.exit(1)


def process_url(url: str) -> None:
    """
    Scrape data at a given URL, whether binary or HTML.
    """
    if is_binary_data(url):
        download.download_binary(url)
    else:
        scrape.process_page(url, fullpage=True)


def process_urls(path_str: str) -> None:
    """
    Scrape all URLs for given text file path.
    """
    urls = lib.read_text(path_str)

    print(f"Found URLs: {len(urls)}")

    scrape.setup_driver()
    errors = []

    for url in urls:
        try:
            process_url(url)
        except Exception as e:
            error_msg = f"{url} - {str(e)}"
            errors.append(error_msg)

    scrape.close()
    handle_errors(errors)


def main(args: list[str]) -> None:
    """
    Command-line entry-point.
    """
    if not args:
        print("Required arg: PATH")
        print("Provide a path to a text file of one URL per line")

        sys.exit(0)

    input_path_str = args.pop(0)
    process_urls(input_path_str)


if __name__ == "__main__":
    main(sys.argv[1:])
