#!/usr/bin/python3
"""
This is the 2-matrix_divided module.

The 2-matrix_divided module supplies one function, matrix_divided().
For exemple,
>>> matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
>>> matrix_divided(matrix, 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def divide(x, y):
    return round(x / y, 2)


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix and return the result.
    """
    if div == 0:
        raise ZeroDivisionError('division by zero')
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError('matrix must be a matrix\
 (list of lists) of integers/floats')
    try:
        result = [[divide(element, div) for element in row] for row in matrix]
        return result
    except ZeroDivisionError as e:
        return e
    except TypeError as te:
        return te
