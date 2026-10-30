#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 15:55:12 2026

@author: pc
"""
hrsinpt = input("Enter Hours: ")
rateinpt = input("Enter rate: ")

try: 
    rate = float(rateinpt)
    hrs = float(hrsinpt)
except:
    rate = 0
    hrs = 0
    print("Error during conversion")
    quit()
def computepay(rate,hrs):
    grossPay = 0
    while hrs >= 40:
        grossPay = grossPay + ( rate * 40 )
        hrs = hrs - 40
    grossPay = grossPay + (( rate * hrs ) * 1.5 )
    return grossPay
print ("Pay: " + str(computepay(rate,hrs)))
print ("Pay: ", computepay(rate,hrs))


