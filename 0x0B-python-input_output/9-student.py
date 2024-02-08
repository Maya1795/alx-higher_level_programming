#!/usr/bin/python3
'''class of student'''


class Student:
    '''represtent student class'''
    def __init__(self, first_name, last_name, age):
        '''constractor'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''return dic'''
        return self.__dict__
