# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(4))