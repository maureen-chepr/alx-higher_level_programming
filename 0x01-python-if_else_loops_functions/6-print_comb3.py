#!/usr/bin/python3
for x in range(9):
    for y in range(x+1, 10):
        if x+1 != 9:
            print("{:d}{:d}, ".format(x, y), end="")
        else:
            print("{:d}{:d}".format(x, y))
            x += 1
