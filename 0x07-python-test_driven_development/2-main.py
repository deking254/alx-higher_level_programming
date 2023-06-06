#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided
def checker(matrix, div):
    try:
        print(matrix_divided(matrix, div))
    except Exception as e:
        print(e)
    print(matrix)
