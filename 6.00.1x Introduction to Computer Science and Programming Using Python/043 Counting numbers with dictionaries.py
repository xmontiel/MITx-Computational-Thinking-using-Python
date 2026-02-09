# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 11:14:24 2025

@author: Xuan
"""

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    answer = []
    valueCount = {}
    filtered = []
    
    if aDict == {}:
        return answer
    
    for value in aDict.values():
        valueCount[value] = valueCount.get(value, 0) + 1

    for key in valueCount:
        if valueCount[key] == 1:
            filtered.append(key)

    for key in aDict:
        if aDict[key] in filtered:
            answer.append(key)  
    return sorted(answer)
    
    
    
    
print(uniqueValues({1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}))
print(uniqueValues({1: 1, 2: 1, 3: 1}))
