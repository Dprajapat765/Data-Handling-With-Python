# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 11:02:20 2019

@author: BSDU
"""

"""
Code Challenge
  Name: 
    Formatted String
  Filename: 
    format2.py
  Problem Statement:
    Write a program to print the output in the given format. 
    Take input from the user. 
  Hint:
    Try to serach for some function in the str class using help() and dir()
  Input:
    Welcome to Pink City Jaipur
  Output:
    Welcome*to*Pink*City*Jaipur
"""

# taking input from the user
user_input = input("enter the string (replace space with *):")

# replacing the user input
replaced_string = user_input.replace(" ","*")

print("user input string:",user_input)

print("replaced string:",replaced_string)


''' second method with join '''
# taking the input from the user
user_input = input("enter the string (replace space with *):")

# splitting the character with space
splitted_str = user_input.split(" ")

# printing the splitted text
print("*".join(splitted_str))
