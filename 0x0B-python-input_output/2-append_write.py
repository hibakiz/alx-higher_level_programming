#!/usr/bin/python3
""" write to file module"""


def append_write(filename="", text=""):
    """ write to file function
    Args:
    filename: the file name
    text: the text to write to the file
    """
    with open(filename, 'a') as f:
        x = f.write(text)
        return (x)
