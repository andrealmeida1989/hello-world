#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 10:19:53 2026

@author: pc
"""

largest = None
smallest = None
comparison = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    else:
        try:
            comparison = int(num)
        except:
            print("Invalid input")
    if largest is None or smallest is None:
        largest = comparison
        smallest = comparison
    if comparison > largest:
        largest = comparison
    if comparison < smallest:
        smallest = comparison
        
print("Maximum is ", largest)
print("Minimum is ",smallest)