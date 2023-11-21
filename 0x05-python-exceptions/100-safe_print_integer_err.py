#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    import traceback
    first = "Exception: Unknown format code 'd' for object of type "
    try:
        print("{:d}".format(value))
        return (True)
    except (ValueError, TypeError) :
        if isinstance(value, float):
            dtype = "float"
        elif isinstance(value, complex):
            dtype = "complex"
        elif isinstance(value, str):
            dtype = "str"
        elif isinstance(value, bytes):
            dtype = "bytes"
        elif isinstance(value, bytearray):
            dtype = "bytearray"
        elif isinstance(value, list):
            dtype = "list"
        elif isinstance(value, tuple):
            dtype = "tuple"
        elif isinstance(value, set):
            dtype = "set"
        elif isinstance(value, dict):
            dtype = "dict"
        else:
            dtype = "unknown data type"
        msg = first + "'{}'".format(dtype)
        print(msg, file=sys.stderr)
        return (False)
