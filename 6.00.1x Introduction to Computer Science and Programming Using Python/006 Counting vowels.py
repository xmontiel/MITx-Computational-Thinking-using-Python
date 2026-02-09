# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 11:26:51 2025

@author: Xuan
"""
s = "azcbobobegghakl"
count = 0

for letter in s:
    if letter=="a" or letter=="e" or letter=="i" or letter=="o" or letter=="u":
        count += 1
print("Number of vowels: " + str(count))
    