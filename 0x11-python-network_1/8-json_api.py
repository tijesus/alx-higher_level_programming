#!/usr/bin/python3
""" Post only letters from terminal"""

import requests
import sys

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    letter = ""
    if len(sys.argv) > 1:
        letter = sys.argv[1]

    req = requests.post(url, data={'q': letter})
    req_type = req.headers['Content-Type']
    if req_type == 'application/json':
        req_json = req.json()
        if req_json == {}:
            print("No result")
        else:
            print("[{}] {}".format(req_json['id'], req_json['name']))
    else:
        print("Not a valid JSON")
