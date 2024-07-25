#!/bin/bash
# Makes a request and print a specific message catch me if you can
curl -sX POST -H "X-Special-Header: CatchMe" 0.0.0.0:5000/catch_me
