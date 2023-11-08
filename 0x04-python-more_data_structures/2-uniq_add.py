#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    add = set(my_list)
    for i in add:
        sum += i
    return (sum)
