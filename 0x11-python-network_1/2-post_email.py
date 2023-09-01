#!/usr/bin/python3
"""sends an email to the server"""
from urllib import request, parse
import sys

if __name__ == "__main__":
    new = parse.urlencode({"email": sys.argv[2]})
    with request.urlopen(sys.argv[1], new.encode('ascii')) as req:
        res = req.read()
        print(res.decode('utf-8'))
