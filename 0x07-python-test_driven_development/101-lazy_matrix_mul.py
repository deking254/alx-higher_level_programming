#!/usr/bin/python3
"""a function that multiplies 2 matrices by using the module NumPy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """a function that multiplies 2 matrices by using the module NumPy"""
    a = "m_a must be a list"
    b = "m_b must be a list"
    c = "m_a must be a list of lists"
    d = "m_b must be a list of lists"
    e = "m_a can't be empty"
    f = "m_b can't be empty"
    g = "m_a should contain only integers or floats"
    h = "m_b should contain only integers or floats"
    i = "each row of m_a must be of the same size"
    j = "each row of m_b must be of the same size"
    k = "m_a and m_b can't be multiplied"
    if type(m_a) is not list:
        raise TypeError(a)
    else:
        if type(m_b) is not list:
            raise TypeError(b)
        else:
            for a in m_a:
                if type(a) is not list:
                    raise TypeError(c)
                    return
                else:
                    if len(a) == 0:
                        raise TypeError(e)
                        return
                    else:
                        for z in a:
                            if type(z) is not int and type(z) is not float:
                                raise TypeError(g)
                                return
                            else:
                                length = len(m_a[0])
                                if len(a) != length:
                                    raise TypeError(i)
                                    return
            for a in m_b:
                if type(a) is not list:
                    raise TypeError(d)
                    return
                else:
                    if len(a) == 0:
                        raise TypeError(f)
                        return
                    else:
                        for z in a:
                            if type(z) is not int and type(z) is not float:
                                raise TypeError(h)
                                return
                            else:
                                length = len(m_a[0])
                                if len(a) != length:
                                    raise TypeError(j)
                                    return
    arr_one = np.array(m_a)
    arr_two = np.array(m_b)
    try:
        result_matmul = np.matmul(arr_one, arr_two)
        return (result_matmul)
    except Exception as e:
        print(e)
