#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newA = dict(a_dictionary)
    for key, value in newA.items():
        newA[key] = value * 2
    return newA
