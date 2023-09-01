#!/usr/bin/python3
"""module to use urrllib"""
from urllib import request

if __name__ == "__main__":
    with request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        r = res.read()
        print('Body response:')
        print('    - type: ' + str(r.__class__))
        print('    - content: ' + str(r))
        print('    - utf8 content: ' + r.decode('utf-8'))
