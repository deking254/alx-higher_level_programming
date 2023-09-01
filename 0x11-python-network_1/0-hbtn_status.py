#!/usr/bin/python3
"""module to use urrllib"""
from urllib import request

if __name__ == "__main__":
    with request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        r = res.read()
        print('Body response:')
        print('\t- type: ' + str(r.__class__))
        print('\t- content: ' + str(r))
        print('\t- utf8 content: ' + r.decode('utf-8'))
