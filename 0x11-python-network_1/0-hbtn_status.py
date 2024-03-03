#!/usr/bin/python3
"""script that fetches
https://alx-intranet.hbtn.io/status
"""


import urllib.request


url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as page:
  content = page.read()

print ("Body response:")
print(f"    - type:{type(content)}")
print(f"    - content: {content}")
print(f"    - utf8 content: {content.decode('utf-8')}")
