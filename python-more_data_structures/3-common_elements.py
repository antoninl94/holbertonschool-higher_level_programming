#!/usr/bin/python3
def common_elements(set_1, set_2):
    set1 = list(set_1)
    set2 = list(set_2)
    common = []
    for i in set1:
        for j in set2:
            if i == j:
                common.append(i)
    return common
