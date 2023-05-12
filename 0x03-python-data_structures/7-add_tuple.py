#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tupleadd = ()
    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        tupleadd = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    else:
        if len(tuple_a) == 1:
            tuple_a = (tuple_a[0], 0)
        if len(tuple_a) == 0:
            tuple_a = (0, 0)
        if len(tuple_b) == 1:
            tuple_b = (tuple_b[0], 0)
        if len(tuple_b) == 0:
            tuple_b = (0, 0)
        tupleadd = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return (tupleadd)
