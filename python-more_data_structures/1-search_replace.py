#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(my_list)
    for idx, value in enumerate(new_list):
        if search == value:
            new_list[idx] = replace
    return new_list
