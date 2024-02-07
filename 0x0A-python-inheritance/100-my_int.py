#!/usr/bin/python3
'''class myint'''


class MyInt(int):
    '''change in class of int'''
    def __new__(cls, *args, **kargs):
        '''create new inst.'''
        return super(MyInt, cls).__new__(c, *args, **kargs)

    def __eq__(self, o):
        '''let be !='''
        return int(self) != o

    def __ne__(self, o):
        '''let it be =='''
        return int(self) == o
