#!/usr/bin/python3
"""get the header X-Request-Id"""
from urllib import request
import sys

if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as req:
        print(req.getheader('X-Request-Id'))
