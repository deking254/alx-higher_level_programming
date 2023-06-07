#!/usr/bin/python3
"""a function that multiplies 2 matrices by using the module NumPy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """a function that multiplies 2 matrices by using the module NumPy"""
    arr_one = np.array(m_a)
    arr_two = np.array(m_b)
    try:
        result_matmul = np.matmul(arr_one, arr_two)
        return (result_matmul)
    except Exception as e:
        print(e)
