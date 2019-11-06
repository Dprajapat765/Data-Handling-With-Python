# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 11:32:28 2019

@author: BSDU ADMIN
"""

import json

json_str = """
[{
	"Name": {
		"First Name": "Dinesh",
		"Last Name": "Prajapat"
	},
	"Age": 19,3
	"Department": "ML&AI",
	"Qualification": {
		"10th": "pass",
		"12th": "pass",
		"graduation": null
	},
	"Gender": "Male",
	"Email": "dprajapat567@gmail.com",
	"Aadhar": "370588678335",
	"Mobile": {
		"Father": 7742681572,
		"Mother": null,
		"Self": 8504073374
	},
	"Disability": false,
	"Subjects": ["Python", "AI with Python", "Data Handling", "Machine Learning"]
}]
"""

# find the data type 
print(type(json_str))

# lets parse the string to json 
new_json = json.loads(json_str)

# lets find the all the data from list of the json
new_json[0]

new_json[0]["Name"]
new_json[0]["Name"]["First Name"]

new_json[0]["Mobile"]
new_json[0]["Mobile"]["Self"]





faculty = """{
	"Name": {
		"First Name": "Ashutosh",
		"Last Name": "Pareek"
	},
	"Age": 29,
	"Subject": "IT",
	"Qualification": ["BCA", "MCA", "PhD"],
	"Gender": "Male",
	"Email": "hello.from.ashu@gmail.com"
}"""

#dumps method it convert python string to json string



# save the json string to a file
with open("faculty.json","w") as faculty_json:
    json.dump(faculty,faculty_json)


with open("faculty.json","r") as read_faculty:
    new_faculty = json.load(read_faculty)
    
    r_faculty = json.loads(new_faculty)
    print(r_faculty)



#################################################

import requests

# take input from the user
user = input("enter the name of the city to find its teperature:")

url1 = "http://api.openweathermap.org/data/2.5/weather/"
url2 = "?q="+user
url3 = "&APPID=34f66d3de6236fc90244ae9b017198f2"

# combine the complete url
url = url1+url2+url3
#print(url)

# hit the url
response = requests.get(url)
# print the content of the get
response_content=response.content
# lets convert the binary data to json format
data_json=response.json()
#print(data_json)

# lets get the teperature from the data
temp = data_json["main"]["temp"]
cel_temp = (round(temp-273.11,2))
print("temperature of {} is :".format(user),cel_temp)

wind_speed = data_json["wind"]["speed"]
print("wind speed is:",wind_speed)







"""
Code Challenge
  Name: 
    Currency Converter Convert  from USD to INR
  Filename: 
    currecncyconv.py
  Problem Statement:
    You need to fetch the current conversion prices from the JSON  
    using REST API
  Hint:
    http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y
    Check with http://api.fixer.io/latest?base=USD&symbol=EUR
    
"""

import requests
#user input
user_money = int(input("enter $USD to convert in INR:"))
price = requests.get(url="https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=355b46075dc79b184b37")

#print(price)
curr = price.content
data1 = price.json()
doller = data1["USD_INR"]
convert = doller * user_money
print("${} in INR:".format(user_money),convert)




 









