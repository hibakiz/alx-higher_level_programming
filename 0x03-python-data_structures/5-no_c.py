#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        return "".join([i for i in my_string if i != 'c' and i != 'C'])
