# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 15:56:27 2019

@author: BSDU ADMIN
"""



"""
Code Challenge:
  Name: 
    Bid Plus
  Filename: 
    bid_plus.py
  Problem Statement:
      USE SELENIUM
      Write a Python code to Scrap data and download data from given url.
      url = "https://bidplus.gem.gov.in/bidlists"
      Make list and append given data:
          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)
          
          # Optional - Do not do this
          7. Name of the PDF file
          
     Make a csv file add all data in it.
      csv Name: bid_plus.csv
"""

from selenium import webdriver
from bs4 import BeautifulSoup

url = "https://bidplus.gem.gov.in/bidlists"

browser = webdriver.Chrome("D:\\Dinesh_Prajapat\\Data_handling\\Day_9_Webscrapping_Selenium\\chromedriver.exe")

# enter the url in the address bar
browser.get(url)


# get the bid num
bid_num= browser.find_element_by_xpath('//*[@id="pagi_content"]/div[1]/div[1]/p[1]/a').text

# get the quantity
quat = browser.find_element_by_xpath('//*[@id="pagi_content"]/div[1]/div[2]/p[2]/span').text

#  get the items
items = browser.find_element_by_xpath('//*[@id="pagi_content"]/div[1]/div[2]/p[1]/span').text

# get the start date and tiem
sdate = browser.find_element_by_xpath('//*[@id="pagi_content"]/div[1]/div[4]/p[1]/span').text
sdate[:10]
sdate[11:]

edate = browser.find_element_by_xpath('//*[@id="pagi_content"]/div[1]/div[4]/p[2]/span').text
edate[:10]
edate[11:]

# make the lists of all the elements
bid_number = []
quantity = []
item = []
start_date = []
start_time = []
end_date = []
end_time = []
n = 0
while n<=10:
    # get the bid num
    bid_num= browser.find_element_by_xpath('//*[@id="pagi_content"]/div[1]/div[1]/p[1]/a').text
    bid_number.append(bid_num)
    # get the quantity
    quat = browser.find_element_by_xpath('//*[@id="pagi_content"]/div[1]/div[2]/p[2]/span').text
    quantity.append(quat)
    #  get the items
    items = browser.find_element_by_xpath('//*[@id="pagi_content"]/div[1]/div[2]/p[1]/span').text
    item.append(items)
    # get the start date and tiem
    sdate = browser.find_element_by_xpath('//*[@id="pagi_content"]/div[1]/div[4]/p[1]/span').text
    st_date = sdate[:10]
    start_date.append(st_date)
    st_time = sdate[11:]
    start_time.append(st_time)
    
    edate = browser.find_element_by_xpath('//*[@id="pagi_content"]/div[1]/div[4]/p[2]/span').text
    en_date = edate[:10]
    end_date.append(en_date)
    en_time = edate[11:]
    end_time.append(en_time)
    
    n = n+1


from collections import OrderedDict
col_name = ['Bid Number','Quantity','Items','Start Date','Start Time','End Date','End Time']
col_data = OrderedDict(zip(col_name,[bid_number,quantity,item,start_date,start_time,end_date,end_time]))

import pandas as pd
df = pd.DataFrame(col_data)
df.to_csv('D:\\Dinesh_Prajapat\\Data_handling\\Day_9_Webscrapping_Selenium\\bid_file.csv')





