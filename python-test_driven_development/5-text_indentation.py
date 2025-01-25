#!/usr/bin/python3
"""
This is the 5-text_indentation module.

"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print()
            print()
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
