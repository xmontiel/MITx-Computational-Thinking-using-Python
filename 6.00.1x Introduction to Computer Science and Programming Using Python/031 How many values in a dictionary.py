# -*- coding: utf-8 -*-
"""
Created on Fri Jun 20 19:32:19 2025

@author: Xuan
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(animals)

def how_many(aDict):
    cont = 0
    for aList in aDict.values():
        for aValue in aList:
            cont += 1
    return cont

print(how_many(animals))