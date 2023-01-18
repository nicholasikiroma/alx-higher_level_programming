#!/usr/bin/python3
"""Write a Python script that takes in a URL, sends a request to the URL and
displays the body of the response."""
from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]
    request = requests.get(url)
    err_code = request.status_code
    if err_code >= 400:
        print(f"Error code: {err_code}")
    else:
        print(request.text)
