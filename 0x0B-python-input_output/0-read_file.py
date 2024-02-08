#!/usr/bin/python3
'''read file'''


def read_file(filename=""):
    '''read from file'''
    with open(filename, encoding='UTF8') as f:
        print(f.read(), end="")
