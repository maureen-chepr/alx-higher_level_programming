#!/usr/bin/python3
if __name__ == '__main__':

    from sys import argv
    total_args = 0
    for i in range(1, len(argv)):
        total_args += int(argv[i])
        print(total_args)
