# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 14:19:55 2019

@author: BSDU ADMIN
"""


from  selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as BS

#url = "http://keralaresults.nic.in/sslc2018rgr8364/swr_sslc.htm"
url = "http://keralaresults.nic.in/sslc2019duj946/swr_sslc.htm"


#For Windows System
browser = webdriver.Chrome("D:\\Dinesh_Prajapat\\Data_handling\\Day_9_Webscrapping_Selenium\\chromedriver.exe")
#browser = webdriver.Firefox(executable_path="D:/geckodriver")

# For Mac System
#browser = webdriver.Chrome(executable_path="/Users/sylvester/chromedriver")
#browser = webdriver.Firefox(executable_path="/Users/sylvester/geckodriver")


browser.get(url)

sleep(2)

 
school_code = browser.find_element_by_name("treg")
code="2000"
school_code.send_keys(code)


sleep(2)

#get_school_result = browser.find_element_by_xpath('//*[@id="ctrltr"]/td[3]/input[1]')
get_school_result = browser.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[3]/td[3]/input[1]')

get_school_result.click()


sleep(10)
 
html_page = browser.page_source

soup = BS(html_page,"lxml")

# Now you can add your logic of reading from BeautifulSoup

sleep(10)

tbl = soup.find_all('table')
my_table = soup.find('table',id='Table4')

headings =my_table.find('tr',class_='r4')

td = len(headings.find_all('td'))

# generating list to get all the data form the table

a = []
b = []
c = []
d = []
e = []
f = []
g = []
h = []
i = []
j = []
k = []
l = []
m = []


for row in my_table.findAll('tr'):
    c2 = row.findAll('td')
    if len(c2)==13:
        a.append(c2[0].text.strip())
        b.append(c2[1].text.strip())
        c.append(c2[2].text.strip())
        d.append(c2[3].text.strip())
        e.append(c2[4].text.strip())
        f.append(c2[5].text.strip())
        g.append(c2[6].text.strip())
        h.append(c2[7].text.strip())
        i.append(c2[8].text.strip())
        j.append(c2[9].text.strip())
        k.append(c2[10].text.strip())
        l.append(c2[11].text.strip())
        m.append(c2[12].text.strip())


# using 
from collections import OrderedDict
col_name = ["Reg No","Name","I-lang-I","I-lang-II","Eng","Hindi/GK","SS","Phy","Chem","Bio","Maths","IT","Results"]    
col_data = OrderedDict(zip(col_name,[a[1:],b[1:],c[1:],d[1:],e[1:],f[1:],g[1:],h[1:],i[1:],j[1:],k[1:],l[1:],m[1:]]))

import pandas as pd
df = pd.DataFrame(col_data)
df.to_csv("D:\\Dinesh_Prajapat\\Data_handling\\Day_9_Webscrapping_Selenium\\new_file.csv")




sleep(3)

browser.quit()

