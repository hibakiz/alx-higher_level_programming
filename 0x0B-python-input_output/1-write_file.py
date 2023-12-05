#!/usr/bin/python3
""" write to file module"""


def write_file(filename="", text=""):
    """ write to file function
    Args:
    filename: the file name
    text: the text to write to the file
    """
    with open(filename, 'w') as f:
        x = f.write(text)
        return (x)
