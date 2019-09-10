# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 11:39:58 2019

@author: BSDU
"""


"""
Code Challenge
  Name: 
    Pattern Builder
  Filename: 
    pattern.py
  Problem Statement:
    Write a Python program to construct the following pattern. 
    Take input from User.  
  Input: 
    5
  Output:
    Below is the output of execution of this program.
      * 
      * * 
      * * * 
      * * * * 
      * * * * * 
      * * * * 
      * * * 
      * * 
      * 
"""


user = int(input("enter the number to build a pattern:"))
i = "*"
n = 1
while (n < user):
    print(i*n)
    n = n+1
while (n>0):
    print(i*n)
    n=n-1
    
# using for loop
user = int(input("enter the number to build a pattern:"))

# using the for loop for increasing the pattern 
for i in range(1,user):
    print("*" * i)  
for j in range(user-1,0,-1):
    print("*" * j)










