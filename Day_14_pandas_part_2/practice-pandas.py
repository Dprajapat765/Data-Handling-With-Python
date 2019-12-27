# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 10:22:03 2019

@author: BSDU ADMIN
"""
# Qestion 1
import pandas as pd
import numpy as np
data = pd.read_csv("Automobile.csv")

# find the nan values in the dataset 
data['price'].isnull()
data[data['price'].isnull()]

# handle missing values with fill na method 
# fill the missing values with mean of the salary
data['price'] = data['price'].fillna(data['price'].mean())

# getting the values of price column in a ndarry of numpy
price_array = np.array(data['price'])
price_array

# Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price
print("Minimum Price :", data['price'].min())
print("Maximum Price :", data['price'].max())
print("Average Price :", data['price'].mean())
print("Standard Deviation :", data['price'].std())





# Question 2
import pandas as pd
import numpy as np

df = pd.read_csv("training_titanic.csv")

# find the total number of passengers in the dataset
df['PassengerId'].count()

# find all large families sibsp > 3
l_fam = df[df['SibSp']>3]
len(l_fam)

# finding all the features in the dataset
df.isnull().any(axis=0)
df.info()
df.describe()
df[df['Age'].isnull()]
df[df['Embarked'].isnull()]
df[df['Cabin'].isnull()]


# drop the column which has maximum null values
df['Cabin'].isnull()
df.drop('Cabin',axis=1,inplace=True)
df.info()


# Embarked column feature missing values

# df[df['Embarked'].isnull()] # checking the missing values

df = df.dropna(subset=['Embarked'])


# age column missig values handling
df['Age'] = df['Age'].fillna(method='ffill')

# how many people survived in the disaster
survied_people = df[df['Survived']==1]
plot_survived = len(survied_people)


# how many people died in the disaster
died_people = df[df['Survived']==0]
plot_died = len(died_people)

# plot survived vs dead
import matplotlib.pyplot as plt

ind = np.arange(0,1)
plt.title("Died vs Survived")
plt.xticks([0,1],('Survived','Died'),color='red')
plt1 = plt.bar([0,1],[plot_died,plot_survived],color=['red','green'])
plt.show()


# calcuolate the survival rate 
len(survied_people) / len(df['Survived']) * 100


# calculate the survival priroty 
# calculate the survival ratio of female 
female_survive = df[(df['Survived']==1) & \
                    (df['Sex']=="female")
                ]
#male_survive = df[(df['Survived']==1) & \
#                    (df['Sex']=="male")
#                ]
#len(male_survive)
len(female_survive)

# calculation of survival ratio of female
print("Survival ration of female :\n ")
round(len(female_survive) / len(df['Survived']) * 100,2)

# male survived vs male passed away 
male_passed = df[(df['Survived'] == 0) & \
                    (df['Sex'] == "male")
                ]
print("Male Passed Away: ",len(male_passed))

male_survive = df[(df['Survived']==1) & \
                    (df['Sex']=="male")
                ]
#len(male_survive)
print("Male Survived: ",len(male_survive))
# total male on the ship
#len(df[df["Sex"]=='male'])

# female that survived vs female passed away
female_passed = df[(df['Survived'] == 0) & \
                    (df['Sex'] == "female")
                ]
print("Male Passed Away: ",len(female_passed))


#len(male_survive)
print("Male Survived: ",len(female_survive))
# total male on the ship
#len(df[df["Sex"]=='female'])

'''
plotting the male survive vs the male passed away
'''
import matplotlib.pyplot as plt

plt.title("Male Survived vs Male Passed Away")
plt.xticks([0,1],["Male_Passed","Male Survived"])
plt.bar([0,1],[len(male_passed),len(male_survive)],color=['red','green'])
plt.show()


'''
plotting the female survived vs female passed away
'''
import matplotlib.pyplot as plt
plt.title("Female Survived vs Female Passed Away")
plt.xticks([0,1],["Female_Passed","Female Survived"])
plt.bar([0,1],[len(female_passed),len(female_survive)],color=['red','green'])
plt.show()


# does age play a role in the survival
children_age_role = df[(df['Survived']==1) & \
              (df['Age']<18)
              ]
adult_age_role = df[(df['Survived']==1) & \
              (df['Age']>18)
              ]
# let's find the total survival 
total_survival = df[df['Survived']==1]
# check the percientile values
print("Percentage of Child Survival: \n",len(children_age_role) / len(total_survival) * 100)
# check the percintile values for adult
print("Percentage of Adult Survival: \n",len(adult_age_role) / len(total_survival) * 100)
