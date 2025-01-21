#!/usr/bin/python3
def carre(x):
    return x ** 2


def square_matrix_simple(matrix=[]):
    result = [list(map(carre, row)) for row in matrix]
    return result
