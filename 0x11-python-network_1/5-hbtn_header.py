#!/usr/bin/python3
"""
    similar to qst 1
"""
import requests
import sys


if __name__ == '__main__':
    response = requests.get(sys.argv[1])
    print(response.headers.get('X-Request-Id'))
