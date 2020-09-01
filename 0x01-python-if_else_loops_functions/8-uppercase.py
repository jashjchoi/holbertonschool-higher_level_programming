#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        ch = ord(ch)
        if 97 <= ch <= 123:
            ch = ch - 32
        print("{:c}".format(ch), end="")
    print()
