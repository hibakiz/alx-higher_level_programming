#!/usr/bin/python3
"""script that fetches
https://alx-intranet.hbtn.io/status
"""


import urllib.request
import sys


url = sys.argv[1]

with urllib.request.urlopen(url) as page:
    headers = dict(page.getheaders())
    id = headers.get("X-Request-Id")
    print(id)

