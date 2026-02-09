# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 15:10:18 2025

@author: Xuan
"""

def genPrimes():
    x = 2
    pList = []
    while True:
        for p in pList:
            if (x % p) == 0:
                break
        else:
            yield x
            pList.append(x)       
        x += 1
