__author__ = 'mark'

import math


class Point:
    """Class to define a 'point' object which has x/y cartesian coordinates and its associated methods."""

    def __init__(self, x=0.0, y=0.0):
        """Initial values for x and y, defaults 0.0 in both cases. Note that x and y are private - indicated
        by preceding __. These are manipulated by property decorators in the role of setter and getter."""
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    def __str__(self):
        return "({:.2f}, {:.2f})".format(self.__x, self.__y)

    def __repr__(self):
        return self.__str__()

    def distance(self, other):
        """Calculates distance based on Pythagoras' theorem."""
        return math.sqrt((abs(self.__x - other.x) ** 2 + abs(self.__y - other.y) ** 2))

    def __add__(self, other):
        """Adds two points together. Overloads + operator."""
        return Point(self.x + other.x, self.y + other.y)


p1 = Point(3.1, 4.0)
p2 = Point(6.5, 7.75)
p3 = p1 + p2
dist = p1.distance(p2)

print("p1={}".format(p1))
p1.x += 2
print("p1={}".format(p1))
p1 += p2

print("p1={}, p2={}, p3={}, dist={:2f}".format(p1, p2, p3, dist))
