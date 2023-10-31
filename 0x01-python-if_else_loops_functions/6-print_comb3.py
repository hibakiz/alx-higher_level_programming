#!/usr/bin/python3
i = 0 
j = 1
for i in range(9):
    for j in range(i + 1, 10):
        if i != j:
            print(", ".join(["{}{}".format(i, j)]))
