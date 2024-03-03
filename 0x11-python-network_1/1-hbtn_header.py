#!/usr/bin/python3
"""script that fetches
"""


import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    with urllib.request.urlopen(url) as page:
        headers = dict(page.getheaders())
        id = headers.get("X-Request-Id")
        print(id)
