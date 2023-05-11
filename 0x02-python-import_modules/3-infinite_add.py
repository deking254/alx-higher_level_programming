#!/usr/bin/python3
import sys
if __name__ == '__main__':
    argumentslen = len(sys.argv[1:])
    arguments = sys.argv[1:]
    i = 0
    if argumentslen >= 1:
        for arg in arguments:
            i += int(arg)
    print("{}".format(i))
