#!/usr/bin/python3
''' The sqqure module'''


class Square:
    '''define a squre

    Args:
        sq : the square '''
    sq = {}

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
