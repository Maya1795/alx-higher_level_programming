#!/usr/bin/python3
'''MOdule rectangle'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Rectangle class'''
    def __init__(self, width, height):
        '''const.'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__height = height
        self.__width = width
