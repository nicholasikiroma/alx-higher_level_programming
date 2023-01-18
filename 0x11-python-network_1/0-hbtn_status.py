#!/usr/bin/python3
"""Script fetches https://alx-intranet.hbtn.io/status and prints content"""
from urllib.request import urlopen, Request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urlopen(url) as response:
        body = response.read()
    print("Body response:")
    print(f"\t- type: {type(body)}\n\t- content: {body}")
    print(f"\t- utf8 content: {str(body, 'UTF-8')}")
