#!/usr/bin/python3
"""get the list of candidates"""
import requests
import sys

if __name__ == "__main__":
    a = sys.argv[1]
    b = sys.argv[2]
    token = "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"
    autho = dict(Authorization="Bearer " + token)
    url = 'https://api.github.com/repos/' + b + "/" + a + "/" + "commits"
    with requests.get(url) as res:
        js = res.json()
        i = 0
        for j in js:
            name = j.get('commit').get('author').get('name')
            if i < 10:
                print("{}: {}".format(j.get("sha"), name))
                i = i + 1
            else:
                break
