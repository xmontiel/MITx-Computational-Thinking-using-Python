# -*- coding: utf-8 -*-
"""
Created on Fri Jul 25 18:43:09 2025

@author: Xuan
"""

def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    
    numeros = L.copy()
    num_ant = numeros[0]
    asc = [num_ant]
    des = [num_ant]
    ans_asc = []
    ans_des = []
    answer = []
    
    # Ascendente
    for i in range(1, len(numeros)):
        num = numeros[i]
        if num_ant <= num:
            asc.append(num)
        else:
            if len(ans_asc) < len(asc):
                ans_asc = asc.copy()
            asc = [num]
        num_ant = num
    if len(ans_asc) < len(asc):
        ans_asc = asc.copy()
    
    
    # Descendente
    num_ant = numeros[0]
    des = [num_ant]
    for i in range(1, len(numeros)):
        num = numeros[i]
        if num_ant >= num:
            des.append(num)
        else:
            if len(ans_des) < len(des):
                ans_des = des.copy()
            des = [num]
        num_ant = num
    if len(ans_des) < len(des):
        ans_des = des.copy()
                
    # Asc vs. Des.
    if len(ans_asc) < len(ans_des):
        answer = ans_des
    elif len(ans_asc) > len(ans_des):
        answer = ans_asc
    else:
        if numeros.index(ans_asc[0]) <= numeros.index(ans_des[0]):
            answer = ans_asc
        else:
            answer = ans_des
    
    return sum(answer)

    
print(longest_run([10, 4, 3, 8, 3, 4, 5, 7, 7, 2]))

print(longest_run([5, 4, 10]))