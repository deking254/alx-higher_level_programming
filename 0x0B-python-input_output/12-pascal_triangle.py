#!/usr/bin/python3
"""this module seeks to create pascals trangle"""


def pascal_triangle(n):
    """function that returns a list of lists of integers"""
    outer = []
    for row in range(n):
        inner = []
        for col in range(row + 1):
            if col == 0 or col == row:
                inner.append(1)
            else:
                temp_inner = outer[row - 1]
                inner.append(temp_inner[col - 1] + temp_inner[col])
        outer.append(inner)
    return(outer)
