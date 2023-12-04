#!/usr/bin/python3
""" Sq module"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """sq calss"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
