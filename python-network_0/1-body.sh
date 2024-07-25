#!/bin/bash

# Check if URL argument is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

URL=$1

# Send a GET request and store the response body and status code
response=$(curl -s -o /dev/stderr -w "%{http_code}" "$URL")

# Extract the status code from the response
status_code=$(echo "$response" | tail -n1)

# Display the body if the status code is 200
if [ "$status_code" -eq 200 ]; then
  # Print the response body (excluding the last line which is the status code)
  echo "$response" | head -n -1
else
  echo "Error: Received status code $status_code"
fi
