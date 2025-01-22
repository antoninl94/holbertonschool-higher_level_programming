#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorteddict = dict(sorted(a_dictionary.items(), key=lambda item: item[0]))
    for key in sorteddict:
        print(f"{key}: {sorteddict[key]}")
