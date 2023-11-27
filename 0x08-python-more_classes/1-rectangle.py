#!/usr/bin/python3
''' This is a Rectangle module'''


class Rectangle:
    ''' this is the Rectangle class'''
    def __init__(self, width=0, height=0):
        ''' Rectangle attrub
        Args:
            width: the width is the width of the rec
            height: the height is the height of the rec'''
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        '''Getter'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter
        Args: 
            value: to add the width'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Getter'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter
        Args:
            value: to add the height'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
