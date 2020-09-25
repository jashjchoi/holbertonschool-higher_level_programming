#!/usr/bin/python3
"""
    3-say_my_name.py module
    say_my_name: prints My name is <first name> <last name>
    Return None
"""


def say_my_name(first_name, last_name=""):
    """ prints My name is <first name> <last name>
        checks if first_name is a string
        checks if last_name is a string
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")

    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
