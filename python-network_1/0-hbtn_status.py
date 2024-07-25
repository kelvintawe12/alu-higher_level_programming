#!/usr/bin/python3
"""
This script fetches the status of a given URL and displays details about the response.

The details include:
- Type of the response content
- Raw content
- UTF-8 decoded content
"""

import urllib.request
import urllib.error


class URLFetcher:
    def __init__(self, url):
        """
        Initializes URLFetcher with the URL to fetch.
        """
        self.url = url

    def fetch(self):
        """
        Fetches the content of the URL and displays the type, content, and UT.
        """
        try:
            request = urllib.request.Request(self.url, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.'
            })
            with urllib.request.urlopen(request) as response:
                body = response.read()
                print("Body response:")
                print("\t- type:", type(body))
                print("\t- content:", body)
                print("\t- utf8 content:", body.decode('utf-8'))
        except urllib.error.HTTPError as e:
            print(f"HTTPError: {e.code} {e.reason}")
        except urllib.error.URLError as e:
            print(f"URLError: {e.reason}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'  # Update the URL here as needed
    fetcher = URLFetcher(url)
    fetcher.fetch()
