#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    leng = len(matrix)
    new = [None] * leng
    i = 0
    for mat in matrix:
        new[i] = list(map(lambda x: x**2, mat))
        i += 1
    return (new)
