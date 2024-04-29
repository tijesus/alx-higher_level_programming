#!/usr/bin/python3
"""Fetches url from terminal and sends request"""

import requests
import sys

if __name__ == '__main__':
    req = requests.get(sys.argv[1])
    x_Request_ID = req.headers.get('X-Request-ID')
    print(x_Request_ID)
