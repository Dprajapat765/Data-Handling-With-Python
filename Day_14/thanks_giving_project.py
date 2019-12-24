# importing necessary modules
import pandas as pd

# load the data
df = pd.read_csv('E:\\Dinesh_Prajapat\\Data_handling\\Day_14\\thanksgiving-2015-poll-data.csv')

'''
Discover regional and income-based patterns in what Americans eat for 
    Thanksgiving dinner
'''

# lets merge all the food columns in a single columns
df['combined food'] = df[df.columns[11:51]].apply(
    lambda x: ','.join(x.dropna().astype(str)),
    axis=1
)

df['combined food']











'''
    Convert the column name to single word names
'''

# converting all the column names in a single word name
# store the column names in the list
col_names = df.columns.tolist()
empty_list = []

# use the for loop
for i in range(0,65):
    empty_list.append('col'+str(i))
    
# creating the empty dictionary and converting list to dictionary
empty_dict = {}
for i in range(0,len(empty_list)):
    empty_dict[col_names[i]] = empty_list[i]

# use the rename method to change the name of the columns
df.rename(columns = empty_dict,inplace=True)



'''   
 Using the apply method to Gender column to convert Male & Female
'''

# creating a funciton to converting the gender using loop
# with the function
def gender(gen):
    if gen == 'Male':
        return 0        
    elif gen=='Female':
        return 1

# using the apply method
df['col62'] = df['col62'].apply(gender)

# inline function (with lambda)
df['col62'] = df['col62'].apply(lambda i: 1 if (i=='Female') else 0)



'''
Using the apply method to clean up income
    (Range to a average number, X and up to X, Prefer not to answer to NaN)
'''
# converting the column in the string format
df['col63'] = df['col63'].astype(str)
# import the module
import numpy as np
# replace the values with nan
df['col63'] = df['col63'].replace('Prefer not to answer',np.nan)
# create function to replace the charactors and calculate the average values and return the values
def income(my_str):
    if 'to' in str(my_str):
        my_str = my_str.replace(',','')
        my_str = my_str.replace('$','')
        a,b = my_str.split(" to ")
        return ((float(a) + float(b)) / 2)
    elif (my_str=='$200,000 and up'):
        return  int(200000)

# using the apply method
df['col63'] = df['col63'].apply(income)



'''
    compare income between people who tend to eat homemade cranberry sauce for
    Thanksgiving vs people who eat canned cranberry sauce?
'''
# let's plot the data
# importing the module for plotting
import matplotlib.pyplot as plt

# find all the columns that have homemade in the column and find their mean
len_home = round(df[df['col8'] == 'Homemade' ][['col63','col8']].mean()[0])

# find all the column that have canned in the column and find their mean
len_can = round(df[df['col8'] == 'Canned' ][['col63','col8']].mean()[0])


# plot the xticks bar to compare the income
plt.xticks([0,1],['Homemade','Canned'])
plt.bar([0,1],[len_home,len_can],color=['green','red'])
plt.show()



'''
find the average income for people who served each type of cranberry sauce
    for Thanksgiving (Canned, Homemade, None, etc).
'''
# average income of homemade
avg_income_home = len_home[0]

# avg income of canned
avg_income_can = len_can[0]

# avg income of none 
avg_income_none = round(df[df['col8']=='None'][['col63','col8']].mean()[0])

# avg income of other specify
avg_income_other = round(df[df['col8']=='Other (please specify)'][['col63','col8']].mean()[0])

# lets plot all of them with bar
plt.xticks([0,1,2,3],['Homemade','Canned','None','Other'])
plt.bar([0,1,2,3],[avg_income_home,avg_income_can,avg_income_none,avg_income_other],color=['red','green','blue','black'])
plt.show()



'''
    Do people in Suburban areas eat more Tofurkey than people in Rural areas?
'''
# calculate how many people eat tofurkey in suburban area
suburban_area_people = len(df[(df['col60']=='Suburban') & \
                          (df['col2']=='Tofurkey')
                          ])
# calculate how many people eat tofurkey in rural area
rural_area_people = len(df[(df['col60']=='Rural') & \
                          (df['col2']=='Tofurkey')
                          ])
    
# plotting the bar chart to show the difference
plt.title("Rural vs Suburban")
plt.xticks([0,1],['Rural','Suburban'])
plt.bar([0,1],[rural_area_people,suburban_area_people],color=['red','green'])
plt.show()


'''
    Where do people go to Black Friday sales most often?
'''
# finding how many person will sale on black friday
t = df[df['col57']=='Yes'][['col64','col57']]

# lets get the lables of the chart and store them in the list
labels = t['col64'].unique().tolist()

# remove the last value of the list (nan)
labels.pop()

# convert the list in the tuple
labels = tuple(labels)

# store the values of the the data in a list
values = t['col64'].value_counts().tolist()

# lets plot the pie chart 
plt.pie(values,labels=labels,explode=None)
plt.show()



'''
    Is there a correlation between praying on Thanksgiving and income?
'''
# finding the salary of the people who prayed
pray_avg = df[df['col51']=='Yes'][['col63','col51']].mean()[0]

# find the average salary of the people who had not prayed 
not_pray_avg = df[df['col51']=='No'][['col63','col51']].mean()[0]

# store the values of the both
value = [pray_avg,not_pray_avg]

# plotting the relationship of praying and not praying
plt.title("People Pray vs People Not Pray")
plt.pie(value,labels=['Pray','Not Pray'])
plt.show()



'''
    What income groups are most likely to have homemade cranberry sauce?
'''
# finding the columns that have homemade and salary
grp = df[df['col8'] == 'Homemade' ][['col63','col8']]

# make the group by both the columns
df_grp = df.groupby(['col63','col8'])

# empty list to store values
list1 = []
list2 = []

# for loop to itrate the dictionary items
for i,j in df_grp.groups:
    if j=='Homemade' and i == float(i):
        list1.append(i)
        list2.append(j)
        
# new list to store all the groups
list3 = list(zip(list1,list2))
print(list3)

'''
Verify a pattern:
        People who have Turducken and Homemade cranberry sauce seem to have 
        high household incomes.
        People who eat Canned cranberry sauce tend to have lower incomes, 
        but those who also have Roast Beef have the lowest incomes
'''
# it will return all the values who has roast beef 
df[df['col2']=='Turducken'][['col8','col63','col2']]

# homemade average income
var_one = df[(df['col2']=='Turducken') & \
           (df['col8'] == 'Homemade')
        ].mean()[-1]

# find all the values who has 
df[df['col2']=='Roast beef'][['col63','col8','col2']]

# average income of Canned
var_two = df[(df['col8'] == 'Canned') & \
               (df['col63'] == df['col63'])
        ].mean()[-1]

# average income of canned roast beef
var_three = df[(df['col2'] =='Roast beef') & \
               (df['col8'] == 'Canned') & \
               (df['col63'] == df['col63'])
        ].mean()[-1]


# store the incomes in the list
verify_val = [var_one,var_two,var_three]
# lets plot the values of the 
plt.pie(verify_val,labels=['Homemade','Canned','Roast Beef'])


'''
Find the number of people who live in each area type (Rural, Suburban, etc)
    who eat different kinds of main dishes for Thanksgiving:
'''
# calculate the number of person who live in each area type (Rural, Suburban and Urban)
count_area_person = df['col60'].value_counts().tolist()

# lets find how many people eat different types of dishes on thanksgiving day
q = df.groupby("col60")['col2']

# let's find how many people eat different dishes on thanks giving day
q.apply(lambda x:x.value_counts())

