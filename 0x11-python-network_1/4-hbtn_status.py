#!/usr/bin/python3
"""
    script that fetches https://alx-intranet.hbtn.io/status
"""
import requests


if __name__ == '__main__':
    html = requests.get('https://intranet.hbtn.io/status')
    resp = response.text
    print("Body response:")
    print("\t- type: {}".format(type(resp)))
    print("\t- content: {}".format(resp))
