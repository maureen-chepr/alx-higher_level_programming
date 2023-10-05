#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv

    if len(argv) == 1:
        print("0 arguments.")
    else:
        args = len(argv) - 1
        if args == 1:
            print("1 argument:")
        else:
            print("{:d} arguments:".format(args))

        for i in range(1, len(argv)):
            print("{:d}: {}".format(i, argv[i]))
