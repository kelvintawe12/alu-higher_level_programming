#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL, and displays the.
the X-Request-Id variable found in the header of the response.
"""

import urllib.request
import sys

if __name__ == "__main__":
    # Retrieve the URL from the command line arguments
    url = sys.argv[1]

    # Make the request and handle the response using a with statement
    with urllib.request.urlopen(url) as response:
        # Extract the value of the 'X-Request-Id' from the headers
        x_request_id = response.headers.get('X-Request-Id')
        # Print the value of the 'X-Request-Id' header if it exists
        if x_request_id:
            print(x_request_id)
