#!/usr/bin/python3
"""script that fetches
"""


import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {
            "q": q
            }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        try:
            data = response.json()
            if data:
                print(f"[{data.get('id')}] {data.get('name')}")
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
