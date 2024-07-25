#!/bin/bash
# This script takes a URL as an argument and prints the size of the response body in bytes.
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

URL=$1
# Get the size of the response body using curl
body_size=$(curl -s -w '%{size_download}' -o /dev/null "$URL")

echo $body_size