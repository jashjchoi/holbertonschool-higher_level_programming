#!/usr/bin/python3
def safe_print_integer_err(value):
    from sys import stderr
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as error:
        print("Exception: {}".format(error), file=stderr)
        return False
