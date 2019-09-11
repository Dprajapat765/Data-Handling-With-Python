"""
 dict Comprehension, Generators
"""


"""
DICT COMPREHENSION
"""

"""
Dictionary comprehension takes in a group of values, performs some kind of task on them, 
and returns the result as a Dictionary 

{resulting_keys: resulting_values for iteration in series}
The input for a dictionary comprehension does not have to be a dictionary

Dictionary comprehension is a powerful concept and can be used to substitute for loops and lambda functions.

"""

# dict comprehension to create dict with numbers as values
# {key:value for i in list}

new_dict={str(i):i for i in [1,2,3,4,5]}
print(new_dict)


"""Converting a dictionary from a list"""
words = ['car', 'house', 'plant', 'fisherman', 'picnic', 'rodeo']

# Write a code using simple for loop
word_dict=dict()

for word in words:
    word_dict[word] = len(word)    

print(word_dict)


"""Write a code using using Dict Comprehension"""
word_dict = {word: len(word) for word in words}
print(word_dict)



# Only chaging the value of the dictionary 
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
new_dict = {key: value * 2 for key, value in my_dict.items()}
print(new_dict)



# Changing the key and value of the dictionary 
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
new_dict = {key.upper(): value * 2 for key, value in my_dict.items()}
print(new_dict)



# Conditionals Within Dictionary Comprehensions
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

new_dict = {key: val for key, val in my_dict.items() if val > 2}
print(new_dict)

# With multiple if
new_dict = {key: val for key, val in my_dict.items() if val > 2 if key != 'd'}
print(new_dict)



#the syntax gets switched around once else is involved
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

new_dict = {(key.upper() if val > 2 else key): (val + 10 if val > 3 else val + 20) for key, val in my_dict.items()}
print(new_dict)



#Nested Dictionary Comprehensions
my_dict = {
    'A': {
        'a': 1,
        'b': 2,
        'c': 3},
    'B': {
        'd': 4,
        'e': 5,
        'f': 6}
}
    
new_dict = {outer_key: {inner_key: inner_val * 10 for inner_key, inner_val in outer_val.items()} for outer_key, outer_val in my_dict.items()}
print(new_dict)



"""
Code Challenge

Consider the following problem, where you want to create a new dictionary 
where the key is a number divisible by 2 in a range of 0-10 and 
it's value is the square of the number. 

First write the solution using for loop and then rewrite using Comprehension
"""



"""
Code Challenges
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

Let's suppose you need to create a new dictionary from a given dictionary 
but with items that are greater than 2

In the problem above, what if you have to not only get the items greater than 2 
but also need to check if they are multiples of 2 at the same time. 

"""

"""
Code Challenge
Use a dictionary comprehension to count the length of each word in a sentence.
"""

"""
Code Challenge

For all the numbers 1-1000, use a nested list/dictionary comprehension to find 
the highest single digit any of the numbers is divisible by

"""


"""
GENERATORS
"""

"""
Generators in Python look like functions which returns iterator object
Generator functions allow you to declare a function that behaves like an iterator.
An iterator is an object that can be iterated (looped) upon. 

The yield statement turns a functions into a generator.
A generator is a function which returns a generator object.
This generator object can be seen like a function which produces a sequence of 
results instead of a single object. 
The execution of the code stops when a yield statement has been reached.

"""


# Iterating over a list
ez_list = [1, 2, 3]
for i in ez_list:
    print(i)
    

# Iterating over a string
ez_string = "Generators"
for s in ez_string:
    print(s)


# Iterating over a dictionary
ez_dict = {1 : "First", 2 : "Second"}
for key, value in ez_dict.items():
    print(key, value)

# Internally next() function is called multiple times for the iterables
# Iterables support something called the Iterator Protocol.  ( iter and next )
# lists, strings and dictionaries all follow the Iterator Protocol    
    


# Conversely, objects that do not follow the protocol cannot be used in a for loop
number = 12345
for n in number:
    print(n)
    


expertises = ["Novice", "Beginner", "Intermediate", "Proficient", "Experienced", "Advanced"]

expertises_iterator = iter(expertises)

print(type(expertises_iterator))

 
 
next(expertises_iterator)
next(expertises_iterator)
next(expertises_iterator)
next(expertises_iterator)
next(expertises_iterator)
next(expertises_iterator)

next(expertises_iterator)

#Internally, the for loop also calls the next function and terminates, when it gets StopIteration. 



other_cities = ["Strasbourg", "Freiburg", "Stuttgart", 
                "Vienna / Wien", "Hannover", "Berlin", 
                "Zurich"]

city_iterator = iter(other_cities)
while city_iterator:
    try:
        city = next(city_iterator)
        print(city)
    except StopIteration:
        break

# Or
       
for location in other_cities:
    print(location)





# Difference between a regular function and generator function 
    
# Regular function
def function_a():
    return "a"

# Generator function
def generator_a():
    yield "a"


def city_generator():
    yield("London")
    yield("Hamburg")
    yield("Konstanz")
    yield("Amsterdam")
    yield("Berlin")
    yield("Zurich")
    yield("Schaffhausen")
    yield("Stuttgart")


city = city_generator()

type(city)


print(next(city))
print(next(city))
print(next(city))
print(next(city))
print(next(city))
print(next(city))
print(next(city))
print(next(city))

print(next(city))

city = city_generator()
# Start again generating values

#Generators are iterables themselves. 
for item in city:
    print(item)
    


# Generator Expresssion ( Similar to Comprehension)
my_list = ['a', 'b', 'c', 'd']
gen_obj = (x for x in my_list)

type(gen_obj)

next(gen_obj)

for val in gen_obj:
    print(val)




"""Example of Counting"""
def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1

myCountDown = countdown(10)

type(myCountDown)

next(myCountDown)
next(myCountDown)
next(myCountDown)







""" Example of Primes """

def check_prime(number):    
    for divisor in range(2, int(number ** 0.5) + 1):        
        if number % divisor == 0:            
            return False    
        return True

def Primes(max):    
    number = 1    
    while number < max:        
        number += 1        
        if check_prime(number):            
            yield number

primes = Primes(10)

next(primes)
next(primes)
next(primes)

next(primes)


primes = Primes(10)
for x in primes:    
    print(x)


""" Reading from a long log file """

def gen_records(path):
    with open(path) as handle:
        record = {}
        for line in handle:
            if line == "\n":
                yield record
                record = {}
                continue
            key, value = line.rstrip("\n").split(": ", 1)
            record[key] = value
            
            
for record in gen_records('data.txt'):
    print("{} had {} requests in the past hour".format(
        record["article"], record["requests"]))



"""
Code Challenge 1
Write a generator which computes the running average from the list
[7, 13, 17, 231, 12, 8, 3]
"""



"""
Code Challenge 7

https://github.com/thecbp/blog_data/blob/master/recipeData.csv

The data contains important beer characteristics from brewers around the world, 
including style of beer, alcohol by volume (ABV), and amount of beer produced.

"""


#Web scraping and crawling recursively for a link











    