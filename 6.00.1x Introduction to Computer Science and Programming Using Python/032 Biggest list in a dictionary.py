# -*- coding: utf-8 -*-
"""
Created on Fri Jun 20 21:12:03 2025

@author: Xuan
"""

aDict = {'a': [15, 2], 'c': [18, 13, 10, 11, 10], 'b': [7, 3, 14, 1, 18, 5, 13, 10, 2, 11], 'd': [18]}

def biggest(aDict):
    cont = 0
    subList = []
    for aList in aDict.values():
        cont = len(aList)
        subList.append(cont)  
        posicionMax = subList.index(max(subList))
        indList = list(aDict.keys())
        solucion = indList[posicionMax] 
    return solucion

print(biggest(aDict))


"""
ChatGPT:
def biggest(aDict):
    maxKey = None
    maxLen = -1
    for key in aDict:
        if len(aDict[key]) > maxLen:
            maxLen = len(aDict[key])
            maxKey = key
    return maxKey

print(biggest(aDict))
"""