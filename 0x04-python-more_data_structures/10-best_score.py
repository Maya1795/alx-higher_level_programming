#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    mk = None
    mv = 0
    for k, v in a_dictionary.items():
        if v > mv:
            mv = v
            mk = k
    return mk
