#!/usr/bin/python3
'''Module for lookup method.'''


def lookup(obj):
    '''Know object attr. and methods
    Args:
        object: the list for object

    Returns:
        list
    '''
    return dir(obj)
