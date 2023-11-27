#!/usr/bin/python3
''' This is a Rectangle module'''


class Rectangle:
    ''' this is the Rectangle class'''
    number_of_instances = 0

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
        Rectangle.number_of_instances += 1

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def __str__(self):
        return self.print()

    def __repr__(self):
        return f"{self.__class__.__name__}({self.width}, {self.height})"

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

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.height + self.width)

    def print(self):
        '''print the rec with #'''
        pos = ""
        if self.width == 0 or self.height == 0:
            return pos
        for i in range(self.height):
            for j in range(self.width):
                pos += "#"
            if i != self.height - 1:
                pos += "\n"
        return pos
