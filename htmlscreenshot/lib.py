"""
Lib module.
"""
import datetime
import re
from pathlib import Path


VAR_DIR = Path(__file__).parent / "var"
PDF_DIR = VAR_DIR / "pdf"
PNG_DIR = VAR_DIR / "png"

SLUG_PATTERN = re.compile(r"[\W_]+")

ADD_DATETIME_DEFAULT = False
DATETIME_FORMAT = "%Y-%m-%d--%H:%m"
FILENAME_MAX_LENGTH = 100


def read_text(path_str: str) -> list[str]:
    """
    Return the lines of a given text file.
    """
    path = Path(path_str)

    assert path.exists(), f"Unable to read: {path}"

    with open(path, encoding="utf-8") as f_in:
        text = f_in.read()
        urls = text.splitlines()

    return urls


def slugify(value: str) -> str:
    """
    Convert value to a slug - safe for URLs and filenames.

    Non-ASCII characters and symbols are replaced, so the result is only basic
    alphanumeric and hyphens.
    """
    value = value.encode("ascii", errors="replace").decode()
    value = SLUG_PATTERN.sub("-", value)

    return value.strip("-")


def make_filename(name: str, ext: str, add_datetime: bool) -> str:
    """
    Convert a readable name into a suitable filename for output.

    :param name: Name of file. This will be shortened if needed, to avoid
        getting an error on writing and for readability.
    :param ext: Extension without dot. e.g. '.png'.
    :param add_datetime: If True, add the current date and tiem to the start
        of the filename.
    """
    filename = slugify(name)

    filename = filename[:FILENAME_MAX_LENGTH]

    if not filename.endswith(ext):
        filename = f"{filename}{ext}"

    if add_datetime:
        now = datetime.datetime.now()
        dt_str = now.strftime(DATETIME_FORMAT)
        filename = f"{dt_str}--{filename}"

    return filename
