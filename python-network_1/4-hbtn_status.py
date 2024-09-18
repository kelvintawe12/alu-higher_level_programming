#!/usr/bin/python3
"""python script that Fetches url
using the requests module
"""
import requests


if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    if url.startswith('https://'):
        url = "https://alu-intranet.hbtn.io/status"
    res = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(res.text)))
    print("\t- content: {}".format(res.text))
