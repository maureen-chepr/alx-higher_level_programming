#!/usr/bin/python3
"""
    script that takes in a URL,
    sends a request to the URL,
    and displays the value of the X-Request-Id found
"""
import urllib.request
import sys


if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as response:
        var_found = response.getheader('X-Request-Id')

    print(var_found)
