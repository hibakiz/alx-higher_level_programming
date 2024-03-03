#!/usr/bin/python3
"""script that fetches
"""


import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        request = urllib.request.Request(url)
        with urllib.request.urlopen(request) as page:
            print(page.read().decode("utf-8"))
    except urllib.error.HTTPError as http_error:
        print(f"Error code: {http_error.code}")
