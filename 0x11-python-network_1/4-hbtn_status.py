#!/usr/bin/python3
"""fetches a url using the request package"""
import requests

if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: ' + str(r.text.__class__))
    print('\t- content: ' + r.text)
