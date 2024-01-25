#!/bin/bash
# script that takes in a URL, sends a request and displays size
curl -sI "$1" | grep 'Content-Length:' | cut -c 17-
