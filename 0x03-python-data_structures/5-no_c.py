#!/usr/bin/env python3
def no_c(my_string):
    m = ""
    for i in range(len(my_string)):
        if (my_string[i] != 'c' and my_string[i] != 'C'):
            m += my_string[i]
    return m
