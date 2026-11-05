# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 10:24:41 2026

@author: Xuan
"""

def yieldAllCombos(items):
    """
    Generates all combinations of N items into two bags, whereby each
    item is in one or zero bags.

    Yields a tuple, (bag1, bag2), where each bag is represented as a list
    of which item(s) are in each bag.
    """
    
    N = len(items)

    # enumerate the 3**N possible combinations
    for i in range(3**N):
        bag1 = []
        bag2 = []
        combo = (bag1,bag2)

        for j in range(N):
            # test ternary jth of integer i
            if (i // (3**j)) % 3 == 1:
                bag1.append(items[j])
            elif (i // (3**j)) % 3 == 2:
                bag2.append(items[j])

        yield combo
        
        