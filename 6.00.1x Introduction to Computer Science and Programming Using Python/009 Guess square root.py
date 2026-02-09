# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

x = 23
epsilon = 0.01
step = 0.0001
guess = 0.0

while guess <= x:
    if abs(guess**2 -x) >= epsilon:
        print(abs(guess**2 -x))
        print(guess)
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))
    
    