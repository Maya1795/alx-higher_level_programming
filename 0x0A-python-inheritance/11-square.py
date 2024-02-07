#!/usr/bin/python3
'''MOdule square'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''square class'''
    def __init__(self, size):
        '''const.'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''Area for square'''
        return self.__size ** 2

    def __str__(self):
        '''Represtent string'''
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
