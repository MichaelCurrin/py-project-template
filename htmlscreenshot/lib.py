import re
from pathlib import Path

PATTERN = re.compile(r"[\W_]+")


def read(path_str: str) -> list[str]:
    path = Path(path_str)

    assert path.exists(), f"Unable to read: {path}"

    with open(path) as f_in:
        text = f_in.read()
        urls = text.splitlines()

    return urls


def slugify(value):
    value = value.encode("ascii", errors="replace").decode()

    return PATTERN.sub("-", value)
