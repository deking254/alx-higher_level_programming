#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix != [[]]:
        i = 0
        for mat in matrix:
            if len(mat) > 0:
                for ma in mat:
                    leng = len(mat)
                    i += 1
                    if i < leng:
                        print("{:d}".format(ma), end=" ")
                    else:
                        print("{:d}".format(ma))
                        i = 0
    if matrix == [[]]:
        print()
