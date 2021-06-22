#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 12:28:55 2021

@author: frank

So we are asked to write a function which takes a tupple and I am supposed
to return a tuple with only odd positioned elements

e.g if aTup = ('I', 'am', 'a', 'test', 'tuple') then

    oddTupples(aTup) will return ('I', 'a', 'tuple')

"""

def oddTupples(aTup):

    tupple_length = len(aTup)

    new_tupple = ()

    for i in range(tupple_length):
        if (i+1) % 2 == 1 :
            new_tupple = new_tupple + (aTup[i],)
            #print(new_tupple)

    return new_tupple

