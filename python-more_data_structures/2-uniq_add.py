#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    aux = []
    for i in my_list:
        if i not in aux:
            aux.append(i)
            result = result + i
    return result
