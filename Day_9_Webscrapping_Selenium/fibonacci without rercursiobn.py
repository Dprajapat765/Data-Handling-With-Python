# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 09:12:27 2019

@author: BSDU ADMIN
"""

n=int(input("enter a number "))
a=0
b=1
i=1
print(a)
while i<n:
    c=a+b
    b=a
    a=c
    i=i+1
    print(c)