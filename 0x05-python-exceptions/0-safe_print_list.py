#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if x <= 0 or not my_list:
        return (0)
    for i in range(0, x):
        try:
            my_list[i]
        except IndexError:
            break
        print("{}".format(my_list[i]), end='')
    print()
    return (i + 1)
