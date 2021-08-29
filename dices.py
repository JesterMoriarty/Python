#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 11:17:11 2021

@author: 
"""



"""
Goal = Know how many combinations gives the number 5 when rolling two dices
Problem = Do not know how to calculate the probability
Diagnosis = Instead of probability I can use loops 
Design =  I will loop two lists, greb one item and sum with the other, if 
it is equals to x, add to another list, 
Do it 
"""

dice = []

[dice.append(i+1) for i in range(0,6)]

dice2 = dice.copy()

p = []

for i in dice:
    for j in dice:
        x = dice[i-1]+dice2[j-1]
        if x == 12:
            p.append(x)

p_length= len(p)
   
print(dice)
print(dice2)
print(p_length)