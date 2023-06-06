#!/usr/bin/python3
"""
    Write a function
    that divides 
    all elements of a matrix
"""


def matrix_divided(matrix, div):
    a = "matrix must be a matrix (list of lists) of integers/floats"
    b = "Each row of the matrix must have the same size"
    if type(matrix) is not list:
        raise TypeError(a)
    else:
        new = []
        for l in matrix:
            if type(l) is not list:
                raise TypeError(a)
                return
            else:
                inner = []
                length = len(matrix[0])
                if len(l) != length:
                    raise TypeError(b)
                else:
                    for k in l:
                        if type(k) is not int and type(k) is not float:
                            raise TypeError(a)
                        else:
                            if type(div) is not int and type(div) is not float:
                                raise TypeError("div must be a number")
                            else:
                                if div == 0:
                                    raise ZeroDivisionError("division by zero")
                                else:
                                    inner.append(round(k / div, 2))
                    new.append(inner)
    return (new)
