#!/usr/bin/python3
""" read from a file using json"""

import json


def load_from_json_file(filename):
    """ read from a file using json
    Args:
    my_obj: the object to convert to json
    filename: the file to write to
    """
    with open(filename, 'w') as f:
        return json.load(my_obj, f)
