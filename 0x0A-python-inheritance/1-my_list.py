#!/usr/bin/python3
"""
    1-my_list Module
"""


class MyList(list):
    """MyList Class that inherits from list"""
    def print_sorted(self):
        """Print the list, but sorted (ascending)"""
        print(sorted(self))
