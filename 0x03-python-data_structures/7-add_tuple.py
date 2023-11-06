#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = list(tuple_a)
    b = list(tuple_b)
    sum = []
    new = ()
    if a or b:
        for i in range(0, 2):
            if i >= len(b):
                b.append(0)
            elif i >= len(a):
                a.append(0)
            sum.append(a[i] + b[i])
        new = tuple(sum)
    return (new)
