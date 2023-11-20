#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    import traceback

    try:
        print("{:d}".format(value))
        return (True)
    except ValueError as e:
        msg = "Exception: Unknown format code 'd' for object of type 'str'"
        print(msg, file=sys.stderr)
        return (False)
