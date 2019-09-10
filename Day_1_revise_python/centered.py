# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 12:47:54 2019

@author: BSDU
"""

"""
Code Challenge
  Name: 
    Centered Average
  Filename: 
    centered.py
  Problem Statement:
    Return the "centered" average of an array of integers, which we'll say is 
    the mean average of the values, except ignoring the largest and 
    smallest values in the array. 
    If there are multiple copies of the smallest value, ignore just one copy, 
    and likewise for the largest value. 
    Use int division to produce the final average. You may assume that the 
    array is length 3 or more.
    Take input from user  
  Input: 
    1, 2, 3, 4, 100
  Output:
    3
"""
# taking the input from the user
user2 = input("enter the numbers saperated with space:").split(" ")

# creating a new list
new_list = []

# using for loop to add elements in new list
for i in user2:
    if i not in new_list:
        new_list.append(int(i))
        
# finding the minimum of the list and removing it
#min_value = min(new_list)
        
# remove the minimum values
new_list.remove(min(new_list))

# finding the max of the list 
#max_value = max(new_list)

# remove the maximum of the list
new_list.remove(max(new_list))

# get the avrage of the list 
avg = sum(new_list) / len(new_list)

    