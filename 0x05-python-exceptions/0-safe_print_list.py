#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        int(x)
    except ValueError:
        return (0)
    for i in range(0, x):
        try:
            my_list[i]
        except IndexError as e:
            print()
            return (i)
        print("{:d}".format(my_list[i]), end='')
    print()
    return (i + 1)
