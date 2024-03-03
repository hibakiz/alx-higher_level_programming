#!/usr/bin/python3
"""script that fetches
"""


import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = "https://api.github.com/user"
    email = sys.argv[1]
    password = sys.argv[2]
    auth = HTTPBasicAuth(email, password)
    response = requests.get(url, auth=auth)
    data = response.json()
    print(data.get("id"))
