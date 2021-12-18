"""
Scrape module.

Importable functions and CLI tool for converting a single URL into an image.
"""
# pylint: disable=global-statement,global-variable-not-assigned
import sys
from time import sleep

from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver

from . import lib
from .lib import ADD_DATETIME_DEFAULT, PNG_DIR


EXT = ".png"
FULL_SUFFIX = "FULL"
WAIT_S = 3


driver: WebDriver


def close() -> None:
    """
    Close webdriver.
    """
    global driver
    assert driver, "driver is not defined"

    driver.quit()


def setup_driver() -> None:
    """
    Initialize webdriver.

    We add a timeout to implicitly wait for an element to be found, or a
    command to complete, to improve loading of scripts and images before the
    screenshot is taken.
    """
    global driver

    driver = webdriver.Firefox()
    driver.implicitly_wait(WAIT_S)


def load_page(url: str) -> str:
    """
    Request a given webpage URL using the global driver.

    :return title: Derived from the title on the page or the URL.
    """
    print(f"Requesting with browser: {url}")
    assert url.startswith("http"), f"URL must start with http(s) - got: {url}"

    global driver
    driver.get(url)
    sleep(WAIT_S)

    driver.find_element_by_tag_name("title")

    title = driver.title

    if title:
        print(f"Loaded with title: '{title}'")
    else:
        print("Loaded but no title found")
        title = url
    print()

    return title


def save_screenshot(name: str, fullpage: bool, add_datetime: bool) -> None:
    """
    Take a screenshot of the current view and save it based on the given name.

    :param name: A readable name like the title, or the the URL. This will be
        be converted into suitable filename.
        The PNG suffix for you if missing, as the webdriver requires it.
    :param fullpage: If True, take a fullpage screenshot as a separate image,
        in addition to always doing the partial screenshot.
    :param add_datetime: If True, add datetime to the output name.
    """
    global driver

    slug_filename = lib.make_filename(name, EXT, add_datetime)
    out_path = PNG_DIR / slug_filename

    result_ok = driver.save_screenshot(str(out_path))

    if fullpage:
        fullpage_name = f"{name}-{FULL_SUFFIX}"
        slug_filename = lib.make_filename(fullpage_name, EXT, add_datetime)
        out_path = PNG_DIR / slug_filename

        body_el = driver.find_element_by_tag_name("body")
        result_ok = body_el.screenshot(str(out_path))

    if result_ok is False:
        raise ValueError(f"IO error on current page - name: {name}")


def process_page(url: str, fullpage: bool) -> None:
    """
    Convert a webpage URL into an image.
    """
    name = load_page(url)
    save_screenshot(name, fullpage, ADD_DATETIME_DEFAULT)


def main(args: list[str]) -> None:
    """
    Command-line entry-point.

    TODO: Make fullpage configurable.
    """
    global driver

    if not args:
        print("Required arg: URL")
        sys.exit(0)

    setup_driver()

    url = args.pop(0)

    try:
        process_page(url, fullpage=True)
    finally:
        driver.quit()


if __name__ == "__main__":
    main(sys.argv[1:])
