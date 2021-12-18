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


def write_binary(path: Path, content: bytes) -> None:
    """
    Write given binary data to a file.

    e.g. Write a PDF file.
    """
    with open(path, "wb") as f_out:
        f_out.write(content)


def slugify(value: str) -> str:
    """
    Convert value to a slug - safe for URLs and filenames.

    Strips out any non-ASCII characters.
    """
    value = value.encode("ascii", errors="replace").decode()

    return SLUG_PATTERN.sub("-", value)


def make_filename(name: str, ext: str, add_datetime: bool) -> str:
    """
    Convert a readable name into a suitable filename for output.
    """
    filename = slugify(name)

    if not filename.endswith(ext):
        filename = f"{filename}{ext}"

    if add_datetime:
        now = datetime.datetime.now()
        dt_str = now.strftime(DATETIME_FORMAT)
        filename = f"{dt_str}--{filename}"

    return filename
