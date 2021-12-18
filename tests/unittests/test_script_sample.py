"""
Test script sample.
"""
from htmlscreenshot import lib


def test_make_filename():
    result = lib.make_filename(
        "https://www.abc.org/za/xyz/def/2017/2021.pdf", ".pdf", False
    )

    assert result == "https-www-abc-org-za-xyz-def-2017-2021-pdf.pdf"
