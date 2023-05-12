#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) > 0:
        newlist = [None] * len(my_list)
        for i in range(0, len(my_list)):
            if my_list[i] % 2 == 0:
                newlist[i] = True
            if my_list[i] % 2 != 0:
                newlist[i] = False
        return (newlist)
