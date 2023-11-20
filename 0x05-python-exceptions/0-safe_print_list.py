#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    idx = 0
    if x <= 0 or not my_list:
        return (0)
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end='')
            idx += 1
        except IndexError:
            break
    print()
    return (idx)
