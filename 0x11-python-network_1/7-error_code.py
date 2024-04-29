#!/usr/bin/python3
"""Returning error message when error is"""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    url_request = requests.get(url)
    if url_request.status_code >= 400:
        print('Error code: {}'.format(url_request.status_code))
    else:
        print(url_request.text)
