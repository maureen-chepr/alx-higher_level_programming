#!/usr/bin/python3
"""
    script that takes your GitHub credentials,
    (username and password) and uses,
     GitHub API to display your id
"""
import requests
import sys


if __name__ == '__main__':
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]
    info = (username, password)
    res = requests.get(url, auth=info)
    try:
        print(res.json()['id'])
    except Exception:
        print('None')
