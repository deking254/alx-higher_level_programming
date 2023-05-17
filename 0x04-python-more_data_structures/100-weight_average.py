#!/usr/bin/python3
def weight_average(my_list=[]):
    total = 0
    over = 0
    for my in my_list:
        total += my[0] * my[1]
        over += my[1]
    return (total / over)
