# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 11:36:42 2019

@author: BSDU
"""

'''
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


# use the dict comprehension concept to solve this problmes
'''

my_str = "www.google.com"

dict1 = {}

dict1 = {dict1[i]:dict1[i]+1 if i in dict1 else dict1[i] for i in my_str}

    




"""
Code Challenge

Consider the following problem, where you want to create a new dictionary 
where the key is a number divisible by 2 in a range of 0-10 and 
it's value is the square of the number. 

First write the solution using for loop and then rewrite using Comprehension
"""


# solution using the for loop

my_dict = {'a':0,'s':2,'b':1,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10}

new_dict = {}

for key, value in my_dict.items():
    if value %2 == 0 and range(value,10):
        new_dict[value] = value**2
    
print(new_dict)


# solution using dict comprehension

my_dict = {'a':0,'s':2,'b':1,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10}

new_dict = {value:value**2 for key,value in my_dict.items() if value %2==0 if range(value,10)}

print(new_dict)



"""
Code Challenges
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

Let's suppose you need to create a new dictionary from a given dictionary 
but with items that are greater than 2

In the problem above, what if you have to not only get the items greater than 2 
but also need to check if they are multiples of 2 at the same time. 

"""

# way one with the for loop

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for key, val in dict1.items():
    if val > 2 and val % 2== 0:
        print(key,val)

# way two with the dict comprehension
dict2 = {key:val for key,val in dict1.items() if val > 2 if val %2 == 0}
print(dict2)



"""
Code Challenge
Use a dictionary comprehension to count the length of each word in a sentence.
"""

# dictionary comprehension method to find the length of the eack word
word= "This is Dictionary Comprehension."

word_dict = {i: len(i) for i in word.split(" ")}
print(word_dict)



"""
Code Challenge

For all the numbers 1-1000, use a nested list/dictionary comprehension to find 
the highest single digit any of the numbers is divisible by

"""

list1 = max([i for i in range(1,1000) if i%3==0 if range(i,10)])
print(list1)







"""
Code Challenge 1
Write a generator which computes the running average from the list
[7, 13, 17, 231, 12, 8, 3]
"""

#import csv
## read the csv file
#with open("D:/Dinesh_Prajapat/Data_handling_with_python/Day_4_Dict_comprehension_and_generators_or_iterators/recipeData.csv") as data:
#    csv_reader = csv.reader(data,delimiter=" ")
#    for i in csv_reader:
#        print(i)
#
#
#

my_list = [7, 13, 17, 231, 12, 8, 3]

new_list = []
new_list2 = []
def gen(my_list):
    for i in my_list:
        yield i
a = gen(my_list)
try:
    while True:
        obj2 = next(a)
        #print(obj2)
        new_list.append(obj2)
        avg = sum(new_list) / len(new_list)
        new_list2.append(avg)
except StopIteration:
    pass
finally:
    print("Avg is: \n",new_list2)






my_list = [7, 13, 17, 231, 12, 8, 3]


new_obj = (i for i in my_list)

#type(new_obj)
new_list = []

while True:
    obj = next(new_obj)
    new_list.append(obj)
    avg = sum(new_list) / len(new_list)
    print("average:",avg)
print(new_list)
    



"""
Code Challenge 7

https://github.com/thecbp/blog_data/blob/master/recipeData.csv

The data contains important beer characteristics from brewers around the world, 
including style of beer, alcohol by volume (ABV), and amount of beer produced.

"""


# load the dataset 

def data():
    file = open("D:/Dinesh_Prajapat/Data_handling_with_python/Day_4_Dict_comprehension_and_generators_or_iterators/recipeData.csv",encoding="ISO-8859-1")
    for i in file:
        yield i
data_row = data()
  
list3 = []
try:
    while True:
        obj3 = next(data_row)
#        print(obj3)
        list3.append(obj3)
except:
    pass
finally:
#    print(list3)
    print(list3)























