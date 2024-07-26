#!/usr/bin/python3
"""
ends a request to a given URL and displays the body of the response.
If the HTTP status code is 400 or greater, it prints an error message
with the status code.

Usage:
    ./7-error_code.py <URL>

Requirements:
    - The first argument is the URL.
    - Only requests and sys modules are allowed.
"""

import requests
import sys

"""
The script uses the requests module to send HTTP requests and
the sys module to handle command-line arguments.
"""

if __name__ == "__main__":
    """
    Main execution block. This block is executed when the script is
    run directly. It performs the following actions:
    1. Retrieves the URL from the command-line arguments.
    2. Sends a GET request to the URL.
    3. Checks the HTTP status code of the response.
    4. Prints an error message if the status code is 400 or greater,
       otherwise prints the response body.
    """
    # Retrieve the URL from command-line arguments
    url = sys.argv[1]
    
    # Send a GET request to the specified URL
    response = requests.get(url)

    # Check the HTTP status code and handle accordingly
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
