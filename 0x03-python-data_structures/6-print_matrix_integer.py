#!/usr/bin/env python3
def print_matrix_integer(matrix=[[]]):
    i = []
    if matrix:
        for i in matrix:
            if not i:
                print()
                return
            for j in range(0, len(i)):
                if j < len(i) - 1:
                    print("{} ".format(i[j]), end="")
                else:
                    print("{}".format(i[j]))
