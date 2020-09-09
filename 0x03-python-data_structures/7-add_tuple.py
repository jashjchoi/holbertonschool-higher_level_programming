#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    ta = len(tuple_a)
    tb = len(tuple_b)
    newtup = ()
    for i in range(2):
        if i >= ta:
            a = 0
        else:
            a = tuple_a[i]
        if i >= tb:
            b = 0
        else:
            b = tuple_b[i]
        if (i == 0):
            newtup = (a + b)
        else:
            newtup = (newtup, a + b)
    return (newtup)
