#!/usr/bin/python3
import hidden_4
if __name__ == '__main__':
    for attr in vars(hidden_4):
        if attr[0] != '_' and attr[1] != '_':
            print("{}".format(attr))
