# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 20:32:54 2025

@author: Xuan
"""

hand = ({'u': 1, 'h': 1, 'p': 1, 'm': 2, 'y': 1, 'e': 2})

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    return sum(hand.values())

print(calculateHandlen(hand))