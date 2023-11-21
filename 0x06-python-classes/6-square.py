#!/usr/bin/python3
''' The sqqure module'''


class Square:
    """the start of the class"""

    def __init__(self, size=0, position=(0, 0)):
        """squre attrs.

        Args:
            size: int .
            position: tuple
        """
        self.size = size
        self.position = position

    def __str__(self):
        self.my_print()

    @property
    def size(self):
        """getter"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Ssetter

        Args:
            value: the size.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """postion"""
        return self.__position

    @position.setter
    def position(self, value):
        """Ssetter

        Args:
            value: the size.
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        for i in value:
            if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
                msg = "position must be a tuple of 2 positive integers"
                raise TypeError(msg)
        self.__position = value

    def area(self):
        """calc the area"""
        return (self.__size * self.__size)

    def pos_print(self):
        """spaces and #'s"""
        pos = ""
        if self.size == 0:
            print()
            return
        for w in range(self.position[1]):
            pos += "\n"
        for w in range(self.size):
            for i in range(self.position[0]):
                pos += " "
            for j in range(self.size):
                pos += "#"
            pos += "\n"
        return pos

    def my_print(self):
        """pop version"""
        print(self.pos_print(), end='')
