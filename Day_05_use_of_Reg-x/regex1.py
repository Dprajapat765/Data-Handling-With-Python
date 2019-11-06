# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 14:32:56 2019

@author: admin
"""

"""

Code Challenge
  Name: 
    Regular Expression 1
  Filename: 
    regex1.py
  Problem Statement:
    You are given a string N. 
    Your task is to verify that N is a floating point number.
    Take Input From User

    In this task, a valid float number must satisfy all of the following 
    requirements:  
   
    Number can start with +, - or . symbol.
  Hint: 
    Using Regular Expression 
  Input:
    4  
    4.000
    -1.00
    +4.54
  Output:
    False
    True
    True
    True
"""

import re

user = input("Enter the number")

x = re.match(r"[-+.]*\d\.\d+" ,user)

print(x)