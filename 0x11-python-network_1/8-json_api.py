#!/usr/bin/python3
"""Write a Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter."""
import requests
from sys import argv


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) == 1:
        query = ""
    else:
        query = argv[1]
    payload = {"q": query}
    request = requests.post(url, data=payload)
    try:
        json_data = request.json()
        if json_data:
            print(f"{json_data.get('id')} {json_data.get('name')}")
        else:
            print("No result")
    except requests.exceptions.JSONDecodeError as err:
        print("Not a valid JSON")
