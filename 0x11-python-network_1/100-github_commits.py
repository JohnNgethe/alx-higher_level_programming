#!/usr/bin/python3
"""Script that Takes in Github repo nd owner name to list
10 commits (from the most recent to oldest)"""

import requests
import sys

if __name__ == "__main__":

    req = requests.get('https://api.github.com/repos/{}/{}/commits'
                       .format(sys.argv[2], sys.argv[1]))
    if req.status_code >= 400:
        print('None')
    else:
        for i in req.json()[:10]:
            print("{}: {}".format(i.get('sha'),
                                  i.get('commit').get('author').get('name')))
