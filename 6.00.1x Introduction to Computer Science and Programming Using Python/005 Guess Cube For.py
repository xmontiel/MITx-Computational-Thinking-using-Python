# -*- coding: utf-8 -*-
"""
Created on Tue Jun  3 12:23:25 2025

@author: Xuan
"""

cube = -64

for guess in range(abs(cube)+1):
    if(guess**3 >= abs(cube)):
        break
    
if guess**3 != abs(cube):
    print(str(cube) + " is not a perfect cube")
else:
    if cube < 0:
        guess = -guess
    print("Cube root of " + str(cube) + " is " + str(guess))
