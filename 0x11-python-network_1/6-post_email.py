#!/usr/bin/python3
"""
    similar to qst 2 post email
"""
import requests
import sys


if __name__ == '__main__':
    parameter = {"email": sys.argv[2]}
    req = requests.post(sys.argv[1], data=parameter)
    print(req.text)
