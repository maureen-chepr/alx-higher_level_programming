#!/usr/bin/python3
def search_replace(my_list, search, replace):
    index = 0
    while index < len(my_list):
        if my_list[index] == search:
            my_list[index] = replace
        index += 1
    return my_list
