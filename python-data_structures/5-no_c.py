#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    index = ["c", "C"]

    for i in my_string:
        if i not in index:
            new_string += i
    return new_string
