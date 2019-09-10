# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 11:21:17 2019

@author: BSDU
"""

"""

Code Challenge
  Name: 
    Fizz Buzz
  Filename: 
    fizzbuzz.py
  Problem Statement:
    Write a Python program which iterates the integers from 1 to 100(included). 
    For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". 
    For numbers which are multiples of both three and five print "FizzBuzz". 
  User Input 
    Not required  
  Output:
    1
    2
    Fizz
    4 
    Buzz  
"""

# numbers from 1 to 100
for i in range(41,51):
    if (i % 3 == 0 and i % 5 == 0):
        print("FizzBuzz")
    elif (i % 5 == 0):
        print("Buzz")
    elif (i % 3 ==0):
        print("Fizz")
    else:
        print(i)
