#!/bin/bash
# Sends a series of requests to the specified URL to trigger the response "You got me!"
curl -sL -X PUT -d "user_id=98" 0.0.0.0:5000/catch_me -o /dev/null
curl -sL 0.0.0.0:5000/catch_me | grep "You got me!"
