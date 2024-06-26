#!/usr/bin/python3
"""Returning error message when error is"""

import urllib.parse
import urllib.request
from urllib.error import HTTPError
import sys

if __name__ == '__main__':
    try:
        url = sys.argv[1]
        url_request = urllib.request.Request(url)
        with urllib.request.urlopen(url_request) as resp:
            print(resp.read().decode("ascii"))
    except HTTPError as e:
        print('Error code: {}'.format(e.code))
