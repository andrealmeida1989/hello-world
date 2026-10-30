#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 13:20:56 2026

@author: pc
"""

scoreinpt = input("Enter Score: ")
try:
    score = float(scoreinpt)
except:
    print("error during conversion")
    quit()
if score >= 0.9:
    ScoreGrade = "A"
elif score >= 0.8:
    ScoreGrade = "B"
elif score >=  0.7:
    ScoreGrade = "C"
elif score >=  0.6:
    ScoreGrade = "D"
elif score < 0.6:
    ScoreGrade = "F"
else:
    print("Grade out of bound")
print(ScoreGrade)
#quit()
tot = 0 
for i in [5, 4, 3, 2, 1] :
    tot = tot + 1
print(tot)

