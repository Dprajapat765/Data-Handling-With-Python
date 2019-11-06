# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 15:28:38 2019

@author: BSDU ADMIN
"""


"""
Code Challenge
  Name: 
    Webscrapping ICC Cricket Page
  Filename: 
    icccricket.py
  Problem Statement:
    Write a Python code to Scrap data from ICC Ranking's 
    page and get the ranking table for ODI's (Men). 
    Create a DataFrame using pandas to store the information.
  Hint: 
    https://www.icc-cricket.com/rankings/mens/team-rankings/odi 
    
    
    #https://www.icc-cricket.com/rankings/mens/team-rankings/t20i
    #https://www.icc-cricket.com/rankings/mens/team-rankings/test
"""


from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi").text

data = BeautifulSoup(page)

tbl = data.find('table',class_='table')
tbl_row = tbl.findAll('tr',class_='table-body')
tbl_row
tbl.findAll('td',class_="table-body__cell")


A = []
B = []
C = []
D = []

for row in tbl.findAll('tr'):
    n  = row.findAll('td')
    if len(n)==5:
        A.append(n[1].text.strip())
        B.append(n[2].text.strip())
        C.append(n[3].text.strip())
        D.append(n[4].text.strip())

from collections import OrderedDict
col_name = ["team name",'total matches','points','rating']
col_data = OrderedDict(zip(col_name,[A,B,C,D]))

import pandas as pd
df = pd.DataFrame(col_data)
df.to_csv("D:\\Dinesh_Prajapat\\Data_handling\\Day_9_Webscrapping_Selenium\\odi_ranking_data.csv")




