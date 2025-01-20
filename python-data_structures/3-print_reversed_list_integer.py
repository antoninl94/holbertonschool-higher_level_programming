#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list)):
        if i == len(my_list) - 1:
            break
        i += 1
    while i != -1:
        print("{:d}".format(my_list[i]))
        i -= 1
