#!/usr/bin/python3
""" read from a file using json"""

import json


def load_from_json_file(filename):
    """ read from a file using json
    Args:
    filename: the file to write to
    """
    with open(filename, 'r') as f:
        return json.load(f)
