# -*- coding: utf-8 -*-
"""
Created on Sat Jun  7 15:15:18 2025

@author: Xuan
"""

epsilon = 0.01
y = 9
guess = y/2.0
numGuesses = 0

while abs(guess*guess - y) >= epsilon:
    numGuesses += 1
    guess = guess - (((guess**2) - y)/(2*guess))
print("numGuesses = " + str(numGuesses))
print("Square root of " + str(y) + " is about " + str(guess))
