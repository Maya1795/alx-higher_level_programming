#!/usr/bin/python3
'''Module for rectangle'''
from models.base import Base


class Rectangle(Base):
    '''Rectangle class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''concstractor'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''width of rect'''
        return self.__width

    @width.setter
    def width(self, value):
        self.validation("width", value, False)
        self.__width = value

    @property
    def height(self):
        '''height of rect'''
        return self.__height

    @height.setter
    def height(self, value):
        self.validation("height", value, False)
        self.__height = value

    @property
    def x(self):
        '''x of rect'''
        return self.__x

    @x.setter
    def x(self, value):
        self.validation("x", value)
        self.__x = value

    @property
    def y(self):
        '''y of rect'''
        return self.__y

    @y.setter
    def y(self, value):
        self.validation("y", value)
        self.__y = value

    def validation(self, name, value, eq=True):
        '''Validation method'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be > 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        '''Rectangke area'''
        return self.width * self.height

    def display(self):
        '''retangle display'''
        m = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(m, end='')
