#!/usr/bin/python3
""" write to a file using json"""

import json


def save_to_json_file(my_obj, filename):
    """ write to a file using json
    Args:
    my_obj: the object to convert to json
    filename: the file to write to
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
