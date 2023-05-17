#!/usr/bin/python3
def search_replace(my_list, search, replace):
    leng = len (my_list)
    new = [None] * leng
    i = 0
    for my in my_list:
        if my == search:
            new[i] = replace
        else:
            new[i] = my
        i += 1
    return (new)
