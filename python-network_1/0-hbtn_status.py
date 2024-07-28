#!/usr/bin/python3
"""Displays the url fetched """


import urllib.request


if __name__ == '__main__':
    url = 'https://intranet.hbtn.io/status'
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
