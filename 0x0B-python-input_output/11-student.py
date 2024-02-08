#!/usr/bin/python3
'''class of student'''


class Student:
    '''represtent student class'''
    def __init__(self, first_name, last_name, age):
        '''constractor'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''return dic'''
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        my_dict = dict()
        for k, v in self.__dict__.items():
            if k in attrs:
                my_dict[k] = v
        return my_dict

    def reload_from_json(self, json):
        '''reload json'''
        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value
