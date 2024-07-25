#!/usr/bin/python3
"""
This script fetches the status of a given URL and displays details about the.
"""

import urllib.request


class URLFetcher:
    def __init__(self, url):
        self.url = url

    def fetch(self):
        with urllib.request.urlopen(self.url) as response:
            body = response.read()
            print("Body response:")
            print("\t- type:", type(body))
            print(f"\t- content: {body}")
            print(f"\t- utf8 content: {body.decode('utf-8')}")


if __name__ == "__main__":
    url = 'https://alu-intranet.hbtn.io/status'
    fetcher = URLFetcher(url)
    fetcher.fetch()
