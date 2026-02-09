# -*- coding: utf-8 -*-
"""
Created on Sun Jul 13 16:50:56 2025

@author: Xuan
"""

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    
    def __eq__(self, Coordinate):
        if self.x == Coordinate.x and self.y == Coordinate.y:
            return True
        else:
            return False
        
    def __repr__(self):
        return 'Coordinate(' + str(self.getX()) + ',' + str(self.getY()) + ')'
    
c1 = Coordinate(20,20)
c2 = Coordinate(-14,-14)

print(c1)
print(c2)
print(c1 == c2)
print(repr(c1))
