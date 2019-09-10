# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 13:31:47 2019

@author: BSDU
"""

# taking the input from the user
user = input("enter the numbers saperated by comma:").split(",")

# creating a empty list
new_list = []

# using the for loop 
for i in user:
    if i not in new_list:
        new_list.append(i)

# printing the list        
print(new_list)

# converting the list into tuple
print(tuple(new_list))
        
        
        