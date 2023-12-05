#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for i in matrix:
        if len(i) == 0:
            print()
        for y in range(len(i)):
            print("{:d}".format(i[y]), end="\n" if y is len(i) - 1 else " ")
