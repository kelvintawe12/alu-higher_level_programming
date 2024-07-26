#!/usr/bin/python3
"""
This script fetches the status from https://alu-intranet.hbtn.io/status
and displays the body of the response with specific formatting.

Requirements:
    - Only the requests module is allowed.
    - The response body must be displayed as:
      Body response:
          - type: <class 'str'>
          - content: OK
"""

import requests

if __name__ == "__main__":
    url = 'https://alu-intranet.hbtn.io/status'
    response = requests.get(url)
    body = response.text

    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")
