#!/usr/bin/python3
''' The sqqure module'''


class Square:
    def __init__(self, size=0):
        """squre attrs.

        Args:
            size: int .
        Raises:
            TypeError: integer test
            ValueError: negative test
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Ssetter

        Args:
            value: the size.
        """
        

        self.__size = value

    def area(self):
        """calc the area"""
        return (self.__size * self.__size)
