#!/bin/bash
# Makes a PUT request to the specified URL with a custom header to trigger the expected response
curl -s -X PUT -H "X-Secret-Header: MySecretValue" 0.0.0.0:5000/catch_me
