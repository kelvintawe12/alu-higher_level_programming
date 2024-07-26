#!/usr/bin/python3
s script sends a request to a given URL and displays the body of the
response. If the HTTP status code is 400 or greater, it prints an error
message with the status code.

Usage:
    ./7-error_code.py <URL>

Requirements:
    - The first argument is the URL.
    - Only requests and sys modules are allowed.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
