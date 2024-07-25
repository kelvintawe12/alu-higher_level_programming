#!/bin/bash
# Make a POST request with specific data to trigger the server response
curl -s -X POST -d "user_id=98" -H "Origin: School" 0.0.0.0:5000/catch_me | grep -o "You got me!"
