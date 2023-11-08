#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        maxx = max(a_dictionary.values())
        for i in a_dictionary.keys():
            if a_dictionary[i] == maxx:
                return (i)
    return (None)
