#!/usr/bin/python3
for n in range(0, 100):
    if n != 99:
        print("{}".format(n if n > 9 else "0" + str(n)), end=", ")
    else:
        print("{}".format(n), end="\n")
