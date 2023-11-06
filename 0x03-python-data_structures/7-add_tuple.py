#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = list(tuple_a)
    b = list(tuple_b)
    sum = []
    for i in range(0, len(a)):
        if i >= len(b):
            b.append(0)
        sum.append(a[i] + b[i])
    new = tuple(sum)
    return (new)
