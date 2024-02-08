#!/usr/bin/python3
'''append in file'''


def append_write(filename="", text=""):
    '''append in file'''
    with open(filename, "a", encoding='UTF8') as f:
        return f.write(text)
