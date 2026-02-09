# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 15:58:36 2025

@author: Xuan
"""
testList = [1, -4, 8, -9]

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

def absSquare(a):
    return abs(a**2)

applyToEach(testList, absSquare)

print(testList)
