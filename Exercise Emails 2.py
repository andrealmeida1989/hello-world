
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 14:09:26 2026

@author: pc
"""
count = None
sender = dict()
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
        sender[content[1]] = sender.get(content[1],0) + 1     
        line = None
    else:
        continue
FrequentSender = None
Comparative = 0
# iterate through the dictonary and verify which is the 
for email,count in sender.items():
    if count is None or count > Comparative:
            FrequentSender = email
            Comparative = count
print(FrequentSender,Comparative)
print("There were", count, "lines in the file with From as the first word")
