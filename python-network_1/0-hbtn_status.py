#!/usr/bin/python3
"""
This script fetches the status of a given URL and displays details about the response.

The details include:
- Type of the response content
- Raw content
- UTF-8 decoded content
"""

import urllib.request


class URLFetcher:
    def __init__(self, url):
        """
        Initializes URLFetcher with the URL to fetch.
        """
        self.url = url

    def fetch(self):
        """
        Fetches the content of the URL and displays the type, content, and UTF-8 content.
        """
        with urllib.request.urlopen(self.url) as response:
            body = response.read()
            print("Body response:")
            print("\t- type:", type(body))
            print("\t- content:", body)
            print("\t- utf8 content:", body.decode('utf-8'))

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'  # Update the URL here as needed
    fetcher = URLFetcher(url)
    fetcher.fetch()

