# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 14:37:33 2019

@author: BSDU
"""

# Hands On 1  
# Make a function to find whether a year is a leap year or no, return True or False 


def leap_year(year):
    if year % 4 == 0 or year % 400 ==0 and year % 100 == 0:
        return "{} is a leap year". format(year)
    else:
        return '{} is not a leap year'. format(year)
year = int(input("enter year:"))
leap_year(year)



# Hands On 2
# Make a function days_in_month to return the number of days in a specific month of a year

def days_in_month(month_name):
    if month_name in ["january","march","may","july","august","october","december"]:
        return "number of days in this month is {}". format(31)
    
    if month_name in ["april","march",'june','september','november']:
        return "number of days in this month is {}". format(30)
    
    if month_name is "feberuary":
        return "number of days in this month {}".format(28)
        
month_name = input("enter the name of the month:")

days_in_month(month_name)





