# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 10:55:23 2019

@author: BSDU
"""

"""
Code Challenge
  Name: 
    Factorial
  Filename: 
    factorial.py
  Problem Statement:
    Find the factorial of a number. 
  Hint: 
    Factorial of 3 = 3 * 2 * 1= 6 
    Try to first find the function from math module using dir and help 
  Input:
    Take the number from the keyboard as input from the user.
"""

# with the math library
# importing necessary module
import math

# taking input from the use
user_input = int(input("enter any number to find the factorial:"))

# using the factorial function of the library
factorial_value = math.factorial(user_input)

print("factorial of {} is: {}".format(user_input,factorial_value))
