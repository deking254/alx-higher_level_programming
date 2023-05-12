#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) > 0:
        for my in my_list:
            status = 0
            for i in range(0, len(my_list)):
                if my >= my_list[i]:
                    status += 1
            if status == len(my_list):
                return (my)
