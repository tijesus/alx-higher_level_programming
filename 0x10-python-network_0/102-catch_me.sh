#!/bin/bash
# make request to a server updating its response
curl -sX POST -d "You got me!" http://0.0.0.0:5000/catch_me
