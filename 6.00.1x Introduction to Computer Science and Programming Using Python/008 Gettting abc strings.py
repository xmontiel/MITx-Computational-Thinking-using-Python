# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 11:55:28 2025

@author: Xuan
"""

s = 'abc'
cont = 0
char_ant = ""
abc = ""
answer = ""

for char in s:

    if char_ant <= char:
        abc = str(abc+char)
        print(abc)
    elif len(answer) < len(abc):
        answer = abc
        abc = char
        print(answer)
    else:
        abc = char
        print(answer)
    if(len(s) == cont+1):
        if len(answer) < len(abc):
            answer = abc

    cont += 1
    char_ant = s[cont-1]


print("Longest substring in alphabetical order is: " + answer)