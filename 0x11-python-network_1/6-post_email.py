#!/usr/bin/python3
"""sends a POST request to the passed URL with the email"""
import requests
import sys

if __name__ == "__main__":
    payload = dict(email=sys.argv[2])
    with requests.post(sys.argv[1], payload) as res:
        print(res.text)
