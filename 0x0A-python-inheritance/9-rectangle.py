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

    def area(self):
        '''Area method'''
        return self.__width * self.__height

    def __str__(self):
        '''Represtent string'''
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
