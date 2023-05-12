#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    tup = ()
    if length > 0:
        tup = (length, sentence[0])
    else:
        tup = (length, None)
    return (tup)
