#!/usr/bin/python3
""" write to file module with json"""

import json


def to_json_string(my_obj):
    """ write to file function with json
    Args:
    my_obj: the object to convert
    """
    return json.dumps(my_obj)
