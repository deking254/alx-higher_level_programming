#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list:
        length = len(my_list)
        if idx < length and idx >= 0:
            del(my_list[idx])
            return (my_list)
        else:
            return (my_list)
