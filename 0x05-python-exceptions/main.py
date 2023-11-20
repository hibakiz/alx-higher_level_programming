#!/usr/bin/python3
safe_print_list = __import__('0-safe_print_list').safe_print_list

my_list = ['str', 1, 2, 3]

nb_print = safe_print_list(my_list, 1)
print("nb_print: {:d}".format(nb_print))
