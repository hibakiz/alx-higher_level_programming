#!/usr/bin/python3
""" load from a file using json"""

import json
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_file = __import__('6-load_from_json_file').load_from_json_file

    try:
        listt = load_file("add_item.json")
    except FileNotFoundError:
        listt = []
    listt.extend(sys.argv[1:])
    save_to_json_file(listt, "add_item.json")
