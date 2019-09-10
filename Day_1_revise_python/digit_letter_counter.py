# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 13:40:36 2019

@author: BSDU
"""

# demo data
data = "Python 3.7"
dict2 = {"Digit":0,"Letter":0}

for i in data:
    if i.isalpha() == True:
        dict2["Letter"] += 1
    elif i.isdigit()  == True:
        dict2["Digit"] += 1

print(dict2)
        

        
        