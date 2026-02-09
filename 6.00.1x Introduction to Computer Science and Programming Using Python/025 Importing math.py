# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 14:35:19 2025

@author: Xuan
"""

def polysum(n,s):
    import math
    
    area = (0.25 * n * s**2) / math.tan(math.pi / n)
    
    perimeter = n * s
    
    return round(area + perimeter**2, 4)