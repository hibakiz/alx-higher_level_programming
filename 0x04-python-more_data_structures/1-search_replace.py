#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_list2 = my_list.copy()
    for i in range(0, len(my_list2)):
        if my_list2[i] == search:
            my_list2[i] = replace
    return (my_list2)
