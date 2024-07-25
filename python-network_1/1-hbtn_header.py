#!/usr/bin/python3
"""
Fetches the value of the X-Request-Id header from a URL using urllib.
"""

import urllib.request
import sys

# URL is taken from the command line arguments
url = sys.argv[1]

# Making a request to the URL and fetching the response
with urllib.request.urlopen(url) as response:
    # Getting the value of the 'X-Request-Id' header
    x_request_id = response.headers.get('X-Request-Id')
    # Printing the value of the 'X-Request-Id' header
    print(x_request_id)
