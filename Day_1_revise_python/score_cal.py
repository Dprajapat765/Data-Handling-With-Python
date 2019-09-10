# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 10:42:57 2019

@author: BSDU
"""


"""
Code Challenge
  Name: 
    Weighted Score Calculator
  Filename: 
    score_cal.py
  Problem Statement:
    Lets assume there are 3 assignments and 2 exams, each with max score of 100. 
    Respective weights are 10%, 10%, 10%, 35%, 35% . 
    Compute the weighted score based on individual assignment scores.  
  Hint: 
    weighted score = ( A1 + A2 + A3 ) *0.1 + (E1 + E2 ) * 0.35
"""


print("Enter the marks of assignments and exam (Max Marks = 100)>>>")

# take input from the user
first_ass = float(input("enter the marks of 1st assignment:"))

second_ass = float(input("enter the marks of 2nd assignment:"))

third_ass = float(input("enter the marks of 3rd assignment:"))

exam_one = float(input("enter the marks of 1st exam:"))

exam_sec = float(input("enter the marks of 2nd exam:"))

# calculating the individual assignments scores
weighted_score = round(( first_ass + second_ass + third_ass ) * 0.1 + (exam_one + exam_sec ) * 0.35,2)

print("weighted score of individual {}".format(weighted_score))

