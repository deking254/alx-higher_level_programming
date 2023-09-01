#!/usr/bin/python3
"""displays yhe body of the response and handles error"""
from urllib import request
import urllib
import sys

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res)
    except (urllib.error.HTTPError) as e:
        print("Error code: " + str(e.getcode()))
