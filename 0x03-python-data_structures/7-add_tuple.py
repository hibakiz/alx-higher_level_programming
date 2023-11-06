#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = list(tuple_a)
    b = list(tuple_b)
    sum = []
    leng = 0
    if len(a) >= len(b):
        leng = len(a)
    else:
        leng = len(b)
    if a or b:
        for i in range(0, leng):
            if i >= len(b):
                b.append(0)
            elif i >= len(a):
                a.append(0)
            sum.append(a[i] + b[i])
        new = tuple(sum)
        return (new)
