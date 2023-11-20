#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if x <= 0:
        return (0)
    for i in range(0, x):
        try:
            my_list[i]
        except IndexError:
            print()
            return (i)
        print("{}".format(my_list[i]), end='')
    print()
    return (i + 1)
