#!/usr/bin/python3
'''MOdule for base class'''


class Base:
    '''representation of base'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''constractor'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base. __nb_objects
