# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 11:51:01 2025

@author: Xuan
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    
    high = 0
    low = 0
    
    if a > b:
        high = a
        low = b
    else:
        low = a
        high = b
        
    result = abs(low)

    
    while result > 0:
        if low%result == 0 and high%result == 0:
            return result
        else:
            result -= 1

print(gcdIter(9, 12))