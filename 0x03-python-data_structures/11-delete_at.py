#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if len(my_list) > 0:
        length = len(my_list)
        newlist = [None] * (length - 1)
        j = 0
        if idx < length - 1:
            for i in range(0, length - 1):
                if i != idx:
                    newlist[j] = my_list[i]
                else:
                    newlist[j] = '\0'
                j += 1
            my_list = []
            return (my_list)
        else:
            return (my_list)
