#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        result = fct(args[0], args[1])
        return (result)
    except Exception as e:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
