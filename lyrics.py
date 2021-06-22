#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# Created on Tue Jun 22 10:00:19 2021
#
# @author: frank
#
# In this assignment - I am supposed to take any lyrics
# I choose "Calum Scott - Biblical (Lyrics)"
#
# and split into words creating a list of words then
#
# 1. I am supposed to find frequence of occurance for each word
# =============================================================================

def my_lyrics_frequency(lyrics):
    my_dictionary={}
    for word in lyrics:
        if (word in my_dictionary):
            my_dictionary[word] += 1
            #print(word)
        else:
            my_dictionary[word] = 1

    return my_dictionary

song = "Didn't know that I'd fall so hard Then my feet left the ground \
Gravity don't make no sense when you're around \
I come up against myself when \
Demons in my head get loud\
I don't know how you do it, but you turn them down \
\
I slip and wonder who I'd be \
If I never found you and you never found me \
Well, I don't wanna see \
\
So won't you give me tonight \
And the rest of your life? \
I wanna have it all with you \
I wanna have it all with you \
And when you open your eyes \
I'll be there by your side \
I wanna have it all with you \
I wanna have it all with you \
 \
'Cause your love is biblical \
Biblical \
It's biblical \
 \
If you ever go to pieces \
Fall between the thunder clouds \
I will put you back together, I won't let you down \
 \
I slip and wonder what I'd do \
If you never found me and I never found you \
I don't know what I'd do \
 \
So won't you give me tonight \
And the rest of your life \
I wanna have it all with you \
I wanna have it all with you \
And when you open your eyes \
I'll be there by your side \
I wanna have it all with you \
I wanna have it all with you \
 \
I wanna have it all \
( I wanna have it all ) \
I wanna have it all \
( I wanna have it all ) \
I wanna have it, I wanna have it all \
 \
' Cause your love is biblical \
It's biblical \
It's biblical \
\
So won't you give me tonight \
And the rest of your life? \
I wanna have it all with you \
I wanna have it all with you \
 \
So come on and give me tonight \
And the rest of your life \
I wanna have it all with you \
I wanna have it all with you \
And when you open your eyes \
I'll be there by your side \
I wanna have it all with you \
I wanna have it all with you \
 \
' Cause your love is biblical \
It's biblical \
It's biblical "

song = song.split(" ")
#print(song)

print(my_lyrics_frequency(song))