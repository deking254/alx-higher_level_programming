#!/usr/bin/python3
"""displays the value of the variable X-Request-Id"""
import requests
import sys

if __name__ == "__main__":
    with requests.get(sys.argv[1]) as res:
        print(res.headers.get('X-Request-Id'))
