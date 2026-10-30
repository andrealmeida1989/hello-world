#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 14:09:26 2026

@author: pc
"""
count = None
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)
count = 0
for line in fh:
#    line.rstrip()
    content = None
    content = line.split()
    if line.startswith("From") and len(content)>2:
        print(content[1])
        count = count +1
        line = None
    else:
        continue
print("There were", count, "lines in the file with From as the first word")
