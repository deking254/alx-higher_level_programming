#!/usr/bin/python3
def uniq_add(my_list=[]):
    summation = 0
    for my in my_list:
        summation += my
        for i in range(0, len(my_list)):
            if my == my_list[i]:
                my_list[i] = 0
    return (summation)
