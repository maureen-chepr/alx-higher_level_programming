#!/usr/bin/python3
for x in range(9):
    for y in range(x+1, 10):
        print("{:d}{:d}, ".format(x, y), end="")
print("89")
