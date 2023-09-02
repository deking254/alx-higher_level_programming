#!/usr/bin/python3
"""the hithub Api used to retrieve users"""
import requests
import sys

if __name__ == "__main__":
    payload = dict(Authorization="Bearer " + sys.argv[2])
    url = 'https://api.github.com/users/' + sys.argv[1]
    with requests.get(url, headers=payload) as res:
        try:
            j = res.json()
            if j:
                if j.get("message") == 'Bad credentials':
                    print(None)
                else:
                    print(j.get('id'))
            else:
                print(None)
        except ValueError:
            pass
