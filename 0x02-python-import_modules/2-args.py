#!/usr/bin/python3

a = 10
b = 5

if __name__ == "__main__":
    from sys import argv
    x = len(argv)
    if x == 1:
        print("0 arguments.")
    else:
        x = x - 1
        print("{} ".format(x), end="")
        if x == 1:
            print("argument:")
        else:
            print("arguments:")
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
