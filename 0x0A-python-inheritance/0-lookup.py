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

    attributes = []

    if hasattr(obj, "__dict__"):
        attributes.extend(obj.__dict__.keys())

    for name, value in obj.__class__.__dict__.items():
        if callable(value):
            attributes.append(name)

    return [attr for attr in attributes]
