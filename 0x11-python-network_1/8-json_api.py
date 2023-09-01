#!/usr/bin/python3
"""the search Api usingthe requaests package"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        payload = dict(q=sys.argv[1])
    else:
        payload = dict(q="")
    with requests.post('http://0.0.0.0:5000/search_user', payload) as res:
        try:
            j = res.json()
            if j:
                print('[' + str(j.get('id')) + '] ' + j.get('name'))
            else:
                print('No result')No result
        except ValueError:
            print('Not a valid JSON')
