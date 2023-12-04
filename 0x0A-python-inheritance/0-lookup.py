#!/usr/bin/python3
"""
lookup module
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object.
    Returns:
        A list containing the names of attributes and methods.
    """

    return dir(obj)
