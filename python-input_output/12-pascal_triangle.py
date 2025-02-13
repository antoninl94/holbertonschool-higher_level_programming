#!/usr/bin/python3
"""
This is the ``12-pascal_triangle`` module
"""


def pascal_triangle(n):
    """
    This function return a list of lists of integers
    """
    if n <= 0:
        return
    triangle = [[1]]
    for i in range(1, n):
        previous_row = triangle[-1]
        next_row = [1]
        for j in range(len(previous_row) - 1):
            next_row.append(previous_row[j] + previous_row[j + 1])
        next_row.append(1)
        triangle.append(next_row)
    return triangle
