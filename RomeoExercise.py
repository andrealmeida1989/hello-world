#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 13:54:56 2026

@author: pc
"""

fname = input("Enter file name: ")
#fname = "romeo.txt"
lst = list() 
fh = open(fname)

for line in fh:
    for word in line.split():
        if word not in lst:
            lst.append(word)
        else:
            continue
#    print(line.rstrip())
lst.sort()
print(lst)
    # Split the initial file in the array of strings
    #loop for the array and check if the word exist
    #if the word exist add to a list
    