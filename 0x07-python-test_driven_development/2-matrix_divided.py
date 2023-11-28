#!/usr/bin/python3
'''divide matrix with a num.
    Args:
        matrix (int): The matrix of integer to divide.
        div (int): The num integer to divide.
    Returns: matrix:the matrix members divided with the num'''


def matrix_divided(matrix, div):
    '''divide matrix with a num.
    matrix / b
    '''

    result = []
    i = []
    summ = []
    if len(matrix) != 2:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_lengths = [len(row) for row in matrix]
    if len(set(row_lengths)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    for i in matrix:
        for num in i:
            if not isinstance(num, int) and not isinstance(num, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in range (0, len(matrix)):
        for num in matrix[i]:
            summ.append((round(num / div, 2)))
        result.append(summ)
        summ = []

    return result
