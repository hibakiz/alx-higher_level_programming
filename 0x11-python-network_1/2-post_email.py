#!/usr/bin/python3
"""script that fetches
"""


import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    data = f"email={sys.argv[2]}"
    encoded = data.encode("utf-8")
    request = urllib.request.Request(url, data=encoded, method="POST")
    with urllib.request.urlopen(request) as page:
        print(page.read().decode("utf-8"))
