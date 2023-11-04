#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list) - 1, -1, -1):
        if my_list[i] not None:
            print("{:d}".format(my_list[i]))
