#!/usr/bin/python3
'''class myint'''


class MyInt(int):
    '''change in class of int'''
    def __new__(c, *args, **kargs):
        '''create new inst.'''
        return super(MyInt, c).__new__(c, *args, **kargs)

    def __equailty__(self, o):
        '''let be !='''
        return int(self) != o

    def __new__(self, o):
        '''let it be =='''
        return int(self) == o
