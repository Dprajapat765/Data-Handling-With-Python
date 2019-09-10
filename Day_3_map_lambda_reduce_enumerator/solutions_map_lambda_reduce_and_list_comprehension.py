# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 10:16:30 2019

@author: BSDU
"""

'''

# code challange 1
Find all of the numbers from 1-1000 that are divisible by 7

'''
# way 1
demo_list = []
for i in range(1,1000):
    if i % 7 == 0:
        demo_list.append(i)
print(demo_list)


# compressed way 
my_list = [n for n in range(1,1000) if n % 7 == 0]
print(my_list)



'''

# code challange 2 
Find all of the numbers from 1-1000 that have a 3 in them

'''

list1 = []

#for i in range(1,1000):
#    if i in 
    
print(list1)

num = [x for x in range(1,1000) if x == 3]
print(list(num))

'''

# code challange 3
Count the number of spaces in a string

'''

str1 = "This is a string. "
space = 0
for i in str1:
    if i == " ":
        space += len(i)
print(space)    
 

space_counter = [len(x) for x in str1 if x == " "]
print(len(list(space_counter)))




"""
Code Challenge
  Filename: 
    map1.py
  Problem Statement:
      import random

    names = ['Mary', 'Isla', 'Sam']
    code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']

    for i in range(len(names)):
        names[i] = random.choice(code_names)

    print (names)

As you can see, this algorithm can potentially assign the same secret code name to multiple secret agents. 


Rewrite the above code using map and lambda.


"""


import random

names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']

# way 1 with for loop

for i in range(len(names)):
    names[i] = random.choice(code_names)

print (names)
#===========================================================
# way 2 list comprehension
random_list = map(lambda names: random.choice(code_names), code_names )

print(list(random_list))





"""
Code Challenge
  Filename: 
    map2.py
  Problem Statement:

      names = ['Mary', 'Isla', 'Sam']

    for i in range(len(names)):
        names[i] = hash(names[i])

    print (names)



(Hopefully, the secret agents will have good memories and won’t forget each other’s secret code names during the secret mission.)


Rewrite the above code using map.
    

"""


names = ['Mary', 'Isla', 'Sam']

for i in range(len(names)):
    names[i] = hash(names[i])

print (names)


# way 2  with list comprehension
new_hash = [hash(x) for x in names]
print(new_hash)

# way 3 with the map function 
def hash_name(x):
    return hash(x)


hash2 = map(hash_name,names)
print(list(hash2))


hashed_names = map(lambda names: hash(names),names)
print(list(hashed_names))






"""
Code Challenge
  Filename: 
    height.py
  Problem Statement:

      people = [{'name': 'Mary', 'height': 160},
                {'name': 'Isla', 'height': 80},
                {'name': 'Sam'}]

    height_total = 0
    height_count = 0
    for person in people:
        if 'height' in person:
            height_total += person['height']
            height_count += 1

    if height_count > 0:
        average_height = height_total / height_count

        print (average_height)
    
Try rewriting the code below using map, reduce and filter. 
Filter takes a function and a collection. 
It returns a collection of every item for which the function returned True.
    

"""


'''
people = [{'name': 'Mary', 'height': 160},
                {'name': 'Isla', 'height': 80},
                {'name': 'Sam'}]

height_total = 0
height_count = 0
for person in people:
    if 'height' in person:
        height_total += person['height']
        height_count += 1

if height_count > 0:
    average_height = height_total / height_count
    print (average_height)
'''

# ===========================================
# way 2

people = [{'name': 'Mary', 'height': 160},
                {'name': 'Isla', 'height': 80},
                {'name': 'Sam'}]

#avg_height = map(lambda x:x['height'], filter(lambda x['height']: if x['height'] in people), people)







"""
Code Challenge
  Name: 
    Book Shop
  Filename: 
    book_shop1.py
  Problem Statement:
    Imagine an accounting routine used in a book shop.
    It works on a list with sublists, which look like this:
        
    Order Number  Book Title  Author Quantity  Price per Item
    34587 Learning Python, Mark Lutz  4 40.95
    98762 Programming Python, Mark Lutz 5 56.80
    77226 Head First Python, Paul Barry 3 32.95
    88112 Einführung in Python3, Bernd Klein  3 24.99    
    
    Write a Python program, 
    A) which returns Order Summary as a list with 2-tuples. 
       Each tuple consists of the order number and the product of the price per items 
       and the quantity. 
    
       The product should be increased by 10 INR if the value of the order is smaller 
    than 100.00 INR.

  Hint: 
    Write a Python program using lambda and map.

"""

books = [    [   34587, 'Learning Python', 'Mark Lutz',  4, 40.95],
             [   98762, 'Programming Python', 'Mark Lutz', 5, 56.80],
             [   77226, 'Head First Python', 'Paul Barry', 3, 32.95],
             [   88112, 'Einführung in Python3', 'Bernd Klein',  3, 24.99]
        ]


ord_num = list(map(lambda x: x[0],books))

total_price = list(map(lambda y: y[4]*y[3],books))
# add 10 more money in the price which is less then 100 
add_price =  [round(i+10,2) for i in total_price if i < 100]

# list(map(lambda x: x +10 if x < 100, total_price))


zipped_list = zip(ord_num,total_price)

print(list(zipped_list))

#new_list = map(lambda x: x[0],filter(lambda y:y[3],books),filter(lambda y: y[4],books),books)

#print(list(new_list))








"""
This Python function accepts a list of numbers and computes the product of all the odd numbers:

def productOfOdds(list):
    result = 1
    for i in list:
        if i % 2 == 1:
            result *= i
    return result
    
Rewrite the Python code using map, filter, and reduce:

def productOfOdds(list):
    return reduce(r_func, filter(f_func, map(m_func, list)))

    
"""

from functools import reduce

# define the all three function
def r_func(list):
    result = 1
    for i in list1:
        if i % 2 == 1:
            result *= i
    return result

def f_func(list):
    result = 1
    for i in list1:
        if i % 2 == 1:
            result *= i
    return result

def m_func(list):
    result = 1
    for i in list1:
        if i % 2 == 1:
            result *= i
    return result

def productOfOdds(list):
    return reduce(r_func, filter(f_func, map(m_func, list)))




list = [1,2,3,4,5,6,7,8,9]

productOfOdds(list)





















