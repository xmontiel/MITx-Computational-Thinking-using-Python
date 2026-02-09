# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 06:50:06 2025

@author: Xuan
"""

def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
   try:
       return item / denom
   except ZeroDivisionError:
       return 0

