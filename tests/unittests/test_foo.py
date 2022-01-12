"""
Test foo module.
"""
from pyproject.foo import greet


def test_greet():
    assert greet() == "Hello, World"

    assert greet("Python dev") == "Hello, Python dev"
