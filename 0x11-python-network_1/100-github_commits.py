#!/usr/bin/python3
"""Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""
from sys import argv
import requests


if __name__ == "__main__":
    repo_name = argv[1]
    owner = argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo_name)
    request = requests.get(url)
    js = request.json()
    i = 0
    try:
        while i < 10:
            sha = js[i].get('sha')
            name = js[i].get('commit').get('author').get('name')
            print(f"{sha}: {name}")
            i += 1
    except IndexError:
        pass
