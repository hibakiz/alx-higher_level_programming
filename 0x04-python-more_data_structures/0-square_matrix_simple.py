#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mat = []
    new_list = []
    new = matrix.copy
    for listt in matrix:
        for num in listt:
            new_list.append(num*num)
        new_mat.append(new_list)
        new_list = []
    return (new_mat)
