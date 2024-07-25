#!/bin/bash
# This script sends a request to 0.0.0.0:5000/catch_me and expects to receive "You got me!" in the response.
curl -sL -X PUT -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
