#!/usr/bin/python3
"""
Module for fetching and displaying the status of a URL.

This module contains a class `URLFetcher` which fetches data from a specified
and provides details about the response including the type, content, and UTF-8
decoded content.
"""

import urllib.request

class URLFetcher:
    """
    A class used to fetch and display the status of a URL.

    ...

    Attributes
    ----------
    url : str
        the URL to fetch

    Methods
    -------
    fetch():
        Fetches the content of the URL and displays information about the response.
    """

    def __init__(self, url):
        """
        Constructs all the necessary attributes for the URLFetcher object.

        Parameters
        ----------
            url : str
                the URL to fetch
        """
        self.url = url

    def fetch(self):
        """
        Fetches the content of the URL and displays the type, content, and utf
        This method uses urllib to open the URL and read the response. It the
        the type of the response content, the raw content, and the UTF-8
        """
        with urllib.request.urlopen(self.url) as response:
            body = response.read()
            print("Body response:")
            print("\t- type:", type(body))
            print("\t- content:", body)
            print("\t- utf8 content:", body.decode('utf-8'))


if __name__ == "__main__":
    url = 'https://alu-intranet.hbtn.io/status'
    fetcher = URLFetcher(url)
    fetcher.fetch()
