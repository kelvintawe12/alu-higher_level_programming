#!/usr/bin/python3
"""
This script sends a POST request to a given URL with an email as a parameter.
The email is sent in the variable 'email'. The script then displays the body
of the response.

Usage:
    ./6-post_email.py <URL> <email>

Requirements:
    - The first argument is the URL.
    - The second argument is the email address.
    - Only requests and sys modules are allowed.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    response = requests.post(url, data=data)
    print(response.text)
