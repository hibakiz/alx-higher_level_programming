#!/usr/bin/python3
"""
MyList module
"""


class MyList(list):
    """ print a sorted list
    no Args no Return
    """

    def print_sorted(self):
        """print soreted"""
        print(sorted(self))
