#!/usr/bin/python3
""" Rectangle module"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """BaseGeometry Rec class"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """calc the area for rec"""
        return self.__width * self.__height

    def __str__(self):
        """print and str"""
        strr = "[" + str(self.__class__.__name__) + "] "
        strr += str(self.__width) + "/" + str(self.__height)
        return strr
