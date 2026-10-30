#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 18:08:16 2026

@author: pc
"""

# Use words.txt as the file name
#fname = input("Enter file name: ")
#try:
#    fh = open(fname)
#    Text = fh.read()
#    Text = Text.strip()
#except:
#    print("Error Reading the file")
#print(Text.upper())


# Use the file name mbox-short.txt as the file name
count = 0
Somatory = 0.0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count +1
    Somatory = Somatory + float(line[21:26])
print("Average spam confidence:", Somatory/count)