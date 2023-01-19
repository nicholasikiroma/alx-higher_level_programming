#!/usr/bin/python3
"""Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""
from sys import argv
import requests


if __name__ == "__main__":
    author = argv[1]
    repo = argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(author, repo)
    request = requests.get(url)
    js = request.json()
    i = 0
    while i < 10:
        sha = js[i].get('sha')
        owner = js[i].get('commit').get('author').get('name')
        print(f"{sha}: {owner}")
        i += 1
