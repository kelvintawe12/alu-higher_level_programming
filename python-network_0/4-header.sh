#!/bin/bash
# Send GET request with custom header and check response
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1" | grep -q "Hello Holberton School!" && echo "OK" || echo "FAIL"
