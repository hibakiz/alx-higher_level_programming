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

    def to_json(self, attrs=None):
        """get a dict of the Student
        """
        if (type(attrs) is list and
                all(type(i) is str for i in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
