#!/usr/bin/python3
"""
This script sends a POST request to a specified URL with an email as a param
The email is sent using the 'email' variable in the request body.
The script then prints the body of the response, decoded in UTF-8.

Usage:
    ./2-post_email.py <URL> <email>

Example:
    ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com

Requirements:
    - The first argument is the URL.
    - The second argument is the email address.
    - Only urllib and sys modules are allowed.
    - The script must use the with statement.
"""

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))
