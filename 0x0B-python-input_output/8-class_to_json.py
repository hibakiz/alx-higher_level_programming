#!/usr/bin/python3
"""class to JSON module"""


def class_to_json(obj):
    """class to JSON
    Args:
        obj to convert """
    return obj.__dict__
