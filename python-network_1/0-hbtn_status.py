#!/usr/bin/python3
"""Displays the URL fetched and its content."""


import urllib.request
import urllib.error


def fetch_url(url):
    """Fetches the URL and prints its content."""
    headers = {'User-Agent': 'Mozilla/5.0'}
    request = urllib.request.Request(url, headers=headers)
    
    try:
        with urllib.request.urlopen(request) as response:
            content = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(content)))
            print("\t- content: {}".format(content))
            print("\t- utf8 content: {}".format(content.decode("utf-8")))
    except urllib.error.HTTPError as e:
        print("HTTPError: {}".format(e.code))
    except urllib.error.URLError as e:
        print("URLError: {}".format(e.reason))

if __name__ == '__main__':
    # Fetching from 'https://intranet.hbtn.io/status'
    fetch_url('https://intranet.hbtn.io/status')
    
    # Fetching from 'http://0.0.0.0:5050/status'
    fetch_url('http://0.0.0.0:5050/status')
