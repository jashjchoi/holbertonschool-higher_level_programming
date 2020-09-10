#!/usr/bin/python3
def best_score(a_dictionary):
    best_n = 0
    winner = None
    if type(a_dictionary) is dict:
        for (key, value) in a_dictionary.items():
            if value > best_n:
                best_n = value
                winner = key
    return winner
