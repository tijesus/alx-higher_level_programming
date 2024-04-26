#!/bin/bash
# make request to a server updating its response
curl -X POST -d "You got me!" -H "Content-Type: text/plain" http://0.0.0.0:5000/catch_me
