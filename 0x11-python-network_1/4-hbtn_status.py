#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    request = requests.get(url)
    response = request.text
    print("Body response:")
    print(f"\t- type: {type(response)}\n\t- content: {response}")
