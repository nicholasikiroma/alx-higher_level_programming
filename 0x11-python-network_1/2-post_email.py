#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the
response (decoded in utf-8)"""
import urllib.request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    data = {"email": argv[2]}
    urlencode_data = urllib.parse.urlencode(data)
    post_data = urlencode_data.encode("utf-8")
    url = argv[1]
    with urllib.request.urlopen(url, post_data) as response:
        body = response.read()
    print(body.decode("utf-8"))
