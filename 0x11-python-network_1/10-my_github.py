#!/usr/bin/python3
"""Script that Takes in Github credentials (username and password)
and uses the Github API to display an id"""

import requests
import sys

if __name__ == "__main__":

    req = requests.get('https://api.github.com/user',
                       auth=(sys.argv[1], sys.argv[2]))
    if req.status_code >= 400:
        print('None')
    else:
        print(req.json().get('id'))
