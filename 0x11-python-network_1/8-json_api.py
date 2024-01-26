#!/usr/bin/python3
"""
    script that takes in a letter,
    sends a POST request,
    with the letter as a parameter.
"""
import requests
import sys


if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    try:
        value = sys.argv[1]
    except Exception:
        value = ""
    q = {"q": value}
    res = requests.post(url, data=q)
    try:
        result = res.json()
    except Exception:
        print("Not a valid JSON")
        exit()
    try:
        print("[{}] {}".format(result['id'], result['name']))
    except Exception:
        print("No result")
