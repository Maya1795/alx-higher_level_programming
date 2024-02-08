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
        try:
            for a in attrs:
                if type(a) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        my_dict = dict()
        for k, v in self.__dict__.items():
            if k in attrs:
                my_dict[key] = v
        return my_dict
