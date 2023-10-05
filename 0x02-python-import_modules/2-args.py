#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    x = 1
    while x < len(argv):
        print(f"{x} argument: {argv[x]}")
        x += 1
    else:
        print("0 arguments.")
