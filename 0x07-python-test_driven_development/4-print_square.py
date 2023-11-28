#!/usr/bin/python3
'''print sq.
    Args:
    first_name: The first name.
    last_name: The last name.
    Returns: no returns'''


def print_square(size):
    '''print the user name
    strings
    '''
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
