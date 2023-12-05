#!/usr/bin/python3
""" decode from json"""

import json


def from_json_string(my_str):
    """ decode from  json
    Args:
    my_str: the object to convert from json
    """ 
    return json.loads(my_str)
