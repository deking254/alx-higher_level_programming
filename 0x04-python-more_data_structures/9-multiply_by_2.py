#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    diction = list(a_dictionary.items())
    new = a_dictionary.copy()
    for d in range(0, len(diction)):
        diction[d] = (diction[d][0], diction[d][1] * 2)
    new.update(diction)
    return (new)
