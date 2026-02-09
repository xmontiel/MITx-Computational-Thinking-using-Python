# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 13:30:15 2025

@author: Xuan
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if aStr == "":
        return False
    elif char == aStr[round(len(aStr)/2)]:
        return True
    elif char < aStr[round(len(aStr)/2)]:
        return isIn(char, aStr[0:round(len(aStr)/2)])
    else:
        return isIn(char, aStr[(round(len(aStr)/2))+1:len(aStr)])
    
print(isIn('o', 'abchhjkkkklmnouwwxxy'))
    