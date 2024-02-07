#!/usr/bin/python3
'''Add attribute'''


def add_attribute(obj, a, v):
    """add attribute.
    Arges:
        obj : object
        a: name to be added
        v: value of str
    Raise:
        TypeError: can't add new attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, a, v)
