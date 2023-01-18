#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8)."""
import urllib.request
import urllib.error
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            body = response.read()
        print(body.decode("utf-8"))
    except urllib.error.HTTPError as err:
        print(f"Error code: {err.code}")
