#!/usr/bin/python3
"""a function that multiplies 2 matrices"""


def matrix_mul(m_a, m_b):
    """a function that multiplies 2 matrices"""
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
            new = []
            rows1 = len(m_a)
            cols1 = len(m_a[0])
            rows2 = len(m_b)
            cols2 = len(m_b[0])
            for i in range(rows1):
                inner = []
                for j in range(cols2):
                    result = 0
                    for k in range(cols1):
                        result += m_a[i][k] * m_b[k][j]
                    inner.append(result)
                new.append(inner)
            return (new)
