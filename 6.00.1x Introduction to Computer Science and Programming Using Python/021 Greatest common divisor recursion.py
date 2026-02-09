# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 12:41:07 2025

@author: Xuan
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a < 0:
        a = -a
    if b < 0:
        b = -b
        


    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)
    
print(gcdRecur(30, 125))
    

