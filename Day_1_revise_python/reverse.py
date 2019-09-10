# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 11:59:47 2019

@author: BSDU
"""

"""
Code Challenge
  Name: 
    Reverse Function
  Filename: 
    reverse.py
  Problem Statement:
    Define a function reverse() that computes the reversal of a string.
    Without using Python's inbuilt function
    Take input from User  
  Input: 
    I am testing
  Output:
    gnitset ma I  
"""

# input from the user
user = input("enter the string:")
# splitting the string with space
user.split(" ")

# printing the reversed string
print("".join(reversed(user)))
 



