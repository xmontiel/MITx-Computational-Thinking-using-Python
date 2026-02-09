# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 13:08:34 2025

@author: Xuan
"""

def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)