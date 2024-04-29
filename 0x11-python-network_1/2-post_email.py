#!/usr/bin/python3
"""post emailreceived from terminal"""

import urllib.parse
import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value).encode('ascii')
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as resp:
        content = resp.read()
        print(resp.read().decode("utf-8"))
