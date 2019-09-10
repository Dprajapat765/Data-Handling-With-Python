# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 13:17:45 2019

@author: BSDU
"""

# demo string
my_str = "www.google.com"

# creating empty dictionary
dict1 = {}
# using for loop for finding the frequency of the numbers
for i in my_str:
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i] = dict1[i] + 1

# printing the dictionary
print(dict1)