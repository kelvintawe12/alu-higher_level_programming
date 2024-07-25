#!/bin/bash
# Sends a JSON POST request to a URL with the contents of a file and displays the response body
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
