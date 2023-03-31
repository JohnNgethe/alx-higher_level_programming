#!/usr/bin/python3
"""Script that Takes in a URL, sends a request to the URL and
displays the body of the response"""

import urllib.request
from urllib.error import HTTPError
import sys

if __name__ == "__main__":

    try:
        with urllib.request.urlopen(sys.argv[1]) as resp:
            print(resp.read().decode("utf-8"))
    except HTTPError as err:
        print("Error code: {}".format(err.code))
