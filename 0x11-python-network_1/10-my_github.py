#!/usr/bin/python3
"""Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""
from sys import argv
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = argv[1]
    password = argv[2]
    basic_auth = HTTPBasicAuth(username, password)
    request = requests.get(url, auth=basic_auth)
    js = request.json()
    print(js.get('id'))
