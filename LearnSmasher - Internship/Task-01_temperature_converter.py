#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 20:23:29 2023

@author: chinmayakumarpalo
"""

print("Want to convert to celcious or from celcious")
i=input("input t or f accordingly:- ")

if i=='t' or i=='T':
    f=float(input("Enter the temperture in fahrenheit scale:- "))
    print("the temp in celcious scale is, ", ((f-32)*(5/9)))
    
elif i=='F' or i=='f':
    c=float(input("Enter the temperture in celcious scale:- "))
    print("the temp in fahrenheit scale is, ", ((c*(9/5))+32))
    
else:
    print("invalid input")