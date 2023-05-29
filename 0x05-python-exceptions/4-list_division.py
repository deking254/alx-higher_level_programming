#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = [0] * list_length
    for num in range(0, list_length):
        try:
            new[num] = my_list_1[num] / my_list_2[num]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        continue
    return (new)
