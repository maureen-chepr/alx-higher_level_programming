#!/usr/bin/python3
"""
    script that takes 2 arguments
    The first argument will be the repository name
    The second argument will be the owner name
"""
import requests
import sys


if __name__ == '__main__':
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]
    repository_info = owner_name + "/" + repository_name
    url = "https://api.github.com/repos/" + repository_info + "/commits"
    res = requests.get(url)
    commits = res.json()[:10]
    for i in commits:
        comm_sha = i['sha']
        author_name = i['commit']['author']['name']
        print('{}: {}'.format(commit_sha, author_name))
