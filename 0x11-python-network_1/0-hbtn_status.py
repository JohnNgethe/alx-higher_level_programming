#!/usr/bin/python3
"""Script that Fetches https://intranet.hbtn.io/status"""

from urllib.request import urlopen, Request

if __name__ == "__main__":
    req = Request("https://alx-intranet.hbtn.io/status")
    with urlopen(req) as resp:
        body = resp.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf8")))
