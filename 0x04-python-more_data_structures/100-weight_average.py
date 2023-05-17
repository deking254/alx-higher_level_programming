#!/usr/bin/python3
def weight_average(my_list=[]):
    total = 0
    over = 0
    for my in my_list:
        total += my[0] * my[1]
        over += my[1]
    if len(my_list) == 0:
        return (0)
    else:
        return (total / over)
