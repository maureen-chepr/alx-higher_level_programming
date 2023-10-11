#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = list(dict.fromkeys(my_list))
    return sum(unique)
