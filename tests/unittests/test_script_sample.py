"""
Test script sample module.
"""
from pyproject.script_sample import bar, foo


def test_foo():
    assert foo() is None


def test_bar():
    assert bar(0, 0) == 0
    assert bar(5, 8) == 13
