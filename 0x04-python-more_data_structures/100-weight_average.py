#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        num = 0
        x = 0
        for i in my_list:
            num += (i[0] * i[1])
            x += (i[1])
        return (num/x)
    return (0)
