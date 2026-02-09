# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 10:51:53 2025

@author: Xuan
"""

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp < 0:
        exp = -exp
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base * recurPower(base, exp-1)
    
print(recurPower(2, 5))