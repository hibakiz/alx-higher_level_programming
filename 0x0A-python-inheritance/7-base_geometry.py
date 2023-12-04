#!/usr/bin/python3
""" Create an empty class"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """area function"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validation function"""
        if (type(value) is not int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
