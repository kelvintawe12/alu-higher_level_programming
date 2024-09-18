#!/usr/bin/python3
"""
This script sends a request to a given URL and displays the value of the
X-Request-Id variable found in the response headers.

Usage:
    ./5-hbtn_header.py <URL>

Requirements:
    - The first argument is the URL.
    - Only requests and sys modules are allowed.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)
