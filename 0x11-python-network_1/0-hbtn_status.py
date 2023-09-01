#!/usr/bin/python3
"""module to use urrllib"""
from urllib import request

if __name__ == "__main__":
    res = request.urlopen('https://alx-intranet.hbtn.io/status')
    print(res.__class__)
