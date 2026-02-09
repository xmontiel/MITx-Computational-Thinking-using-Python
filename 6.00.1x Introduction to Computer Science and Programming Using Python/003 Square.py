# -*- coding: utf-8 -*-
"""
Created on Tue Jun  3 11:46:58 2025

@author: Xuan
"""

x = 3
ans = 0
itersLeft = x

while(itersLeft != 0):
    ans = ans + x
    itersLeft = itersLeft - 1

print(str(x) + "*" + str(x) + " = " + str(ans))