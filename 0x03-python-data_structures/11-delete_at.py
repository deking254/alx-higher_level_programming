#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if len(my_list) > 0:
        length = len(my_list)
        if idx < length and idx > 0:
            del(my_list[idx])
            return (my_list)
        else:
            return (my_list)
