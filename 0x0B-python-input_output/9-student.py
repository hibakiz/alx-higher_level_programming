#!/usr/bin/python3
"""class Student"""


class Student:
    """Class student."""

    def __init__(self, first_name, last_name, age):
        """Init new Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """get the dictof json"""
        return self.__dict__
