#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            chara = ord(char) - 32
        else:
            chara = ord(char)
        print("{}".format(chr(chara)), end="")
    print()
