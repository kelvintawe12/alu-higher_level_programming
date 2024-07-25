#!/bin/bash
# Usage: ./0-body_size.sh <URL>
# Example: ./0-body_size.sh http://0.0.0.0:5000

if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

URL=$1

# Send a request to the URL and store the size of the response body in bytes
body_size=$(curl -s -w '%{size_download}' -o /dev/null "$URL")

echo $body_size