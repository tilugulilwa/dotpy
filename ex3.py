#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 11:10:12 2021

@author: frank
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

max = 0
for upper_key in animals:
    tem_total = 0
    for inner_key in animals[upper_key]:
        tem_total+=1

    if tem_total > max:
        max = tem_total
        max_key = upper_key

print(max_key)