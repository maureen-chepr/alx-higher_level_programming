#!/usr/bin/python3
"""
    script that takes in a URL and an email,
    sends a POST request to the passed URL,
    and displays the body of the response
"""
import urllib.request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    parameter = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(parameter)
    data = data.encode("ascii")
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        body = response.read()
    print(body.decode("ascii"))
