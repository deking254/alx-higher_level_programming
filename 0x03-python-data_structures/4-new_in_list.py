#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)
    i = 0
    newlist = [None] * length
    if idx < 0 or idx > length - 1:
        return (my_list)
    else:
        for listt in my_list:
            if i != element:
                newlist[i] = listt
            else:
                newlist[i] = element
            i += 1
        return (newlist)
