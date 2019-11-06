# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 13:54:41 2019

@author: admin
"""

"""

Code Challenge
  Name: 
    Simpsons Phone Book
  Filename: 
    simpsons.py
  Problem Statement:
    There are some people with the surname Neu. 
    We are looking for a Neu, but we don't know the first name, 
    we just know that it starts with a J. 
    Let's write a Python script, which finds all the lines of the phone book, 
    which contain a person with the described surname and a first name starting with J. 
 Hint: 
     Use Regular Expressions 
     re.search(r"J.*Neu",line)  
 Solution:
     Jack Neu 555-7666
     Jeb Neu 555-5543
     Jennifer Neu 555-3652
"""

import re

my_file = open('C:\\Users\\admin\\Desktop\\3rd sem\\Forsk\\Day_05\\simpsons_phone_book.txt')
f = my_file.read()
x = re.findall(r"J[a-zA-z]+\sN[a-zA-Z]+\s\d{3}[-]\d{4}" ,f)
print(x)

my_file = open('C:\\Users\\admin\\Desktop\\3rd sem\\Forsk\\Day_05\\simpsons_phone_book.txt')
f = my_file.readlines()
for  i in f:
    x = re.findall(r"J[a-zA-z]+\sN[a-zA-Z]+\s\d{3}[-]\d{4}" ,i)
    if x:
        print(x)