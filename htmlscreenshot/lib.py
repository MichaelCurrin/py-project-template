"""
Lib module.
"""
import re
from pathlib import Path

PATTERN = re.compile(r"[\W_]+")


def read(path_str: str) -> list[str]:
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

    Strips out any non-ASCII characters.
    """
    value = value.encode("ascii", errors="replace").decode()

    return PATTERN.sub("-", value)
