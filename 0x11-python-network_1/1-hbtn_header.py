#!/usr/bin/python3
"""Fetches url from terminal and sends request"""

import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    url_request = urllib.request.Request(url)
    with urllib.request.urlopen(url_request) as resp:
        x_Request_ID = resp.getheader('X-Request-ID')
        print(x_Request_ID)
