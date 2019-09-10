# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 13:02:00 2019

@author: BSDU
"""



"""
Code Challenge
  Name: 
    Reverse Function
  Filename: 
    reverse.py
  Problem Statement:
    Define a function reverse() that computes the reversal of a string.
    Without using Python's inbuilt function
    Take input from User  
  Input: 
    I am testing
  Output:
    gnitset ma I  
"""

user = input("enter any string :")

print("reverse of string:\n",user[::-1])






"""
Code Challenge
  Name: 
    Reverse Function
  Filename: 
    reverse2.py
  Problem Statement:
    Define a function reverse() that computes the reversal of a integer.
    Take input from User  
  Input: 
    -321
  Output:
    -123  
"""

user_input = input("enter the numbers:")

print('reverse of the interger :',user_input[::-1])







"""
Code Challenge
  Name: 
    Translate Function
  Filename: 
    translate.py
  Problem Statement:
    Write a function translate() that will translate a text into "rövarspråket" 
    Swedish for "robber's language". 
    That is, double every consonant and place an occurrence of "o" in between. 
    Take Input from User  
  Input: 
    This is fun
  Output:
    ToThohisos isos fofunon  
"""

def translate(string):
    res = ""
    for i in string:
        if (i=="A" or i=="E" or i=="I" or i=="O" or i=="U" or i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
            res = res + i
        else:
            print(res+ i + 'o' + i)
##            print(i)
#        print(string)
#res = ""
string = "This is fun"
translate(string)
    







"""
Code Challenge
  Name: 
    Operations Function
  Filename: 
    operation.py
  Problem Statement:
    Write following functions for list operations. Take list as input from the User
    Add(), Multiply(), Largest(), Smallest(), Sorting(), Remove_Duplicates(), Print()
    Only call Print() function to display the results in the below displayed 
    format (i.e all the functions must be called inside the print() function 
    and only the Print() is to be called in the main script)

  Input: 
    5,2,6,2,3
  Output:
    Sum = 18
    Multiply = 360
    Largest = 6
    Smallest = 2
    Sorted = [2, 2, 3, 5, 6]
    Without Duplicates = [2, 3, 5, 6]  
"""


new_list = []

while True:
    user = input("enter the number:")
    if user ==" ":
        break
    for i in user:
        if i not in new_list:
            new_list.append(i)


































