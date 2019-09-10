# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:10:23 2019

@author: BSDU
"""

# Hands On 1  
"""
lunch_menu = ["pizza", "sandwich", "sushi", "soup", "salad"]
Since you're super hungry and super excited about lunch,
enumerate over the array and append an "!" ("exclamation mark") 
to each menu item. 
"""

lunch_menu = ["pizza", "sandwich", "sushi", "soup", "salad"]

# add a exclamation mark to each item of the menu
for index,item in enumerate(lunch_menu):
    print(index,item+'!')



# Hands On 2  
"""
nums = [1, 2, 3, 4]
Enumerate over the array and return a new array of the
squares of those numbers.
"""

nums = [1, 2, 3, 4]

for index,i in enumerate(nums,1):
    print(index*i)
    


# Hands On 3  
"""
odds_and_evens = [1, 3, 2, 18, 5, 10, 24]
iterate over the array and return any even numbers. 
iterate over the array and return only the first array element that is odd

"""

odds_and_evens = [1, 3, 2, 18, 5, 10, 24]

for i in odds_and_evens:
    if i % 2 == 0:
        print('even',i)
        break
    for j in odds_and_evens:
        if j % 2 != 0:
            print('odd',j)
            break

# Hands On 5  
"""
famous_cats = ["Maru", "Lil Bub", "Grumpy Cat"]
check and see if the array includes the string "Maru"
"""

famous_cats = ["Maru", "Lil Bub", "Grumpy Cat"]

for index, i in enumerate(famous_cats):
    if i == "Maru":
        print(True)
    else:
        print(False)
        


# Hands On 6
"""
quiet_and_loud = ["hi", "HI", "shhh", "WHAT?!"]
terate over the array to determine if any of the words contained there are loud (upcased).
"""
quiet_and_loud = ["hi", "HI", "shhh", "WHAT?!"]

for index, i in enumerate(quiet_and_loud):
    if i.isupper():
        print("loud")
    else:
        print("quiet")

        
                
# Hands On 4  
"""
cats_and_dogs = ["cat", "cat", "dog", "cat", "dog", "dog"]
We all know that cats and dogs don't get along. 
Iterate over the array and delete the elements that represent dogs.
"""

animal = ["cat", "cat", "dog", "cat", "dog", "dog"]
while True:
    if animal == 'dog':
        animal.pop('dog')
    else:
        print(animal)
        
        
        












