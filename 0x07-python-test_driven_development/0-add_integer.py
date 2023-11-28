#!/usr/bin/python3
'''Adds two integers.
    Args:
        a (int): The first integer to add.
        b (int): The second integer to add.
    Returns: int: The sum of the two integers.'''


def add_integer(a, b=98):
    '''Adds two integers.
    a + b
    '''
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if a == 'inf' or a == '-inf':
        msg = "OverflowError: cannot convert float infinity to integer"
        raise OverflowError(msg)
    if b == 'inf' or b == '-inf':
        raise OverflowError(msg)
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
