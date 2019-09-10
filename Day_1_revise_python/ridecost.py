# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 10:35:31 2019

@author: BSDU
"""

"""
Code Challenge
  Name: 
    Ride Cost Calculator
  Filename: 
    ridecost_cal.py
  Problem Statement:
    Assume you travel 80 km to and fro in a day. 
    Cost of Diesel per litre is 80 INR 
    Your vehicle Fuel Average is 18 km/litre. 
    Now calculate the cost of driving per day to office. 
  Hint: 
"""    

# distance travelled by the car in km 
distance = 160

# cost of the diesel per litre in rupees
cost_of_fuel = 80

# average of the car in km
avg_of_car = 18

# calculating the fuel for travelled distance
fuel_consumed = distance / avg_of_car
print(fuel_consumed)

# calculating the price for the ride in complete day
price = fuel_consumed * cost_of_fuel
print("price of fuel consumed by the car {}".format(price))