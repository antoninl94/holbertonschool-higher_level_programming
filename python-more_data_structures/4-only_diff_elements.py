#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set1 = list(set_1)
    set2 = list(set_2)
    common = []
    for i in set1:
        if i not in set2:
            common.append(i)
    for j in set2:
        if j not in set1:
            common.append(j)
    return common
