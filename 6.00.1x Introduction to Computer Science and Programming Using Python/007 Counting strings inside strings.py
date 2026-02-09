# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 11:33:24 2025

@author: Xuan
"""

s = "azcbobobegghakl"
x=0
y=3
count=0

for len in s:
    if s[x:y] == "bob":
        count += 1
    x+=1
    y+=1
print("Number of times bob occurs is: " + str(count))
