#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    div_test = []
    for i in my_list:
        if i % 2 == 0:
            div_test.append(True)
        else:
            div_test.append(False)
    return div_test
