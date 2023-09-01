#!/usr/bin/python3
"""the hithub Api used to retrieve users"""
import requests
import sys

if __name__ == "__main__":
    payload = dict(Authorization="Bearer " + sys.argv[2])
    url = 'https://api.github.com/users/'
    with requests.get(url + sys.argv[1], payload) as res:
        try:
            j = res.json()
            if j:
                print(j.get('id'))
            else:
                print(None)
        except Exception:
            pass
