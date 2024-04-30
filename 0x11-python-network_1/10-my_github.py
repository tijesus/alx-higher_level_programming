#!/usr/bin/python3
""" Display github id from terminal"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'
    req = requests.get(url, auth=(username, password))

    req_id = r.json().get('id')
    print(req_id)
