#!/usr/bin/python3
for i in range(0, 8):
    for j in range(1 + i, 10):
        print("{:d}{:d}".format(i, j), end=', ')
print("{:d}{:d}".format(1 + i, j))
