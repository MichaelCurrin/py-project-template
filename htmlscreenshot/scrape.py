"""
Scrape module.

Importable functions and CLI tool for converting a single URL into an image.
"""
import sys
from pathlib import Path
from time import sleep

from selenium import webdriver

OUT_DIR = Path(__file__).parent / "var"
WAIT_S = 3

from . import lib

driver = None


def quit():
    global driver

    assert driver, "driver is not defined"

    driver.quit()


def setup_driver():
    global driver
    driver = webdriver.Firefox()

    # This should help on waiting for element.
    driver.implicitly_wait(WAIT_S)


def load(url):
    """
    Request a given webpage URL.

    :return title: Derived from the title on the page or the URL.
    """
    print(url)
    assert url.startswith("http"), f"URL must start with http(s) - got: {url}"

    driver.get(url)

    sleep(WAIT_S)

    driver.find_element_by_tag_name("title")

    title = driver.title

    print(f"Loaded: {url} - '{title}'")

    if not title:
        title = url

    return title


def save(name="test.png"):
    name = lib.slugify(name)

    if not name.endswith(".png"):
        name = f"{name}.png"

    out_path = OUT_DIR / name

    driver.get_screenshot_as_file(str(out_path))


def process(url):
    """
    Convert a webpage URL into an image.
    """
    name = load(url)
    save(name)


def main(args: list[str]) -> None:
    if not args:
        app_dir = Path(__file__)
        print(f"Required arg: URL")
        sys.exit(0)

    setup_driver()

    url = args.pop(0)

    try:
        process(url)
    finally:
        driver.quit()


if __name__ == "__main__":
    main(sys.argv[1:])
