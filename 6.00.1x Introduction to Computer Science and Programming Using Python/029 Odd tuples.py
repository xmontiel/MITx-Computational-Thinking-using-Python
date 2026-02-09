# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 13:23:43 2025

@author: Xuan
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    ans = ()
    cont = 0
    for t in aTup:
        if cont%2 == 0:
            ans = ans + (t,)
        cont += 1      
    return ans

print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))