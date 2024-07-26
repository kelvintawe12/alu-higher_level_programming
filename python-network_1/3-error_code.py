#!/usr/bin/python3
"""
This script sends a request to a specified URL and displays the body of the response, decoded in UTF-8.
It handles HTTP errors and prints the error code if an exception occurs.

Usage:
    ./3-error_code.py <URL>

Example:
    ./3-error_code.py http://0.0.0.0:5000

Requirements:
    - The first argument is the URL.
    - Only urllib and sys modules are allowed.
    - The script must use the with statement.
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
