#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    j = 0
    for listi in my_list:
        j += 1
    for number in range(0, x):
        try:
            if number == x - 1 or number == j - 1:
                print(my_list[number])
                i += 1
                return (i)
            else:
                print(my_list[number], end="")
                i += 1
        except IndexError:
            break
    return (i)
