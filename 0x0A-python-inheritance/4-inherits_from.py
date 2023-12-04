#!/usr/bin/python3
""" inhirites from or not"""


def inherits_from(obj, a_class):
    """ the function to check
    Args: obj and a_class
    """
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
