import sys
from pathlib import Path

from . import lib, scrape


def process(path_str: str) -> None:
    urls = lib.read(path_str)

    print(f"Found URLs: {len(urls)}")
    print(urls)

    scrape.setup_driver()

    try:
        for url in urls:
            scrape.process(url)
    finally:
        scrape.quit()


def main(args: list[str]) -> None:
    if not args:
        app_dir = Path(__file__)
        print(f"Required arg: PATH")
        print("Provide a path to a text file of one URL per line")
        sys.exit(0)

    path_str = args.pop(0)

    process(path_str)


if __name__ == "__main__":
    main(sys.argv[1:])