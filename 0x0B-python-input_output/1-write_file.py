#!/usr/bin/python3
'''write in file'''


def write_file(filename="", text=""):
    '''write in file'''
    with open(filename, "w", encoding='UTF8') as f:
        return f.write(text)
