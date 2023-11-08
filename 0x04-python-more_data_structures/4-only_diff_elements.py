#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    od = 1
    if set_1 or set_2:
        list1 = list(set_1)
        list2 = list(set_2)
        od_list = []
        first_list = []
        sec_list = []
        for i in list1:
            if od:
                for j in list2:
                    if i == j:
                        od = 0
                        break
                if od:
                    first_list.append(i)
                od = 1
        for i in list2:
            if od:
                for j in list1:
                    if i == j:
                        od = 0
                        break
                if od:
                    sec_list.append(i)
                od = 1
        od_list = first_list + sec_list
        return ((od_list))
    return ([])
