#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if set_1 or set_2:
        list1 = list(set_1)
        list2 = list(set_2)
        od_list = []
        for i in list1:
            for j in list2:
                if i == j:
                    list1.remove(i)
                    list2.remove(j)
        od_list = list1 + list2
        return ((od_list))
    return ([])
