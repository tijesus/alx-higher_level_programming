#!/bin/bash
# Display all mathods the server can accept
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-