#!/usr/bin/python3
"""detects the error returned by response"""
import requests
import sys

if __name__ == "__main__":
    with requests.get(sys.argv[1]) as res:
        if res.status_code == 200:
            print(res.text)
        else:
            print('Error code: ' + str(res.status_code))
