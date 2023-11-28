#!/usr/bin/python3
''' Locked class moduel'''


class LockedClass:
    ''' the LockedClass to prevent adding attrubites rather than first name'''
    __slots__ = ['first_name']
