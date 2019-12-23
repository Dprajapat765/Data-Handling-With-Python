"""
Analysis of Salaries Data ( Hand On Activity )

1. Which Male and Female Professor has the highest and the lowest salaries
2. Which Professor takes the highest and lowest salaries.
3. Missing Salaries - should be mean of the matching salaries of those 
   whose service is the same
4. Missing phd - should be mean of the matching service 
5. How many are Male Staff and how many are Female Staff. 
   Show both in numbers and Graphically using Pie Chart.  
   Show both numbers and in percentage
6. How many are Prof, AssocProf and AsstProf. 
   Show both in numbers adn Graphically using a Pie Chart
7. Who are the senior and junior most employees in the organization.
8. Draw a histogram of the salaries divided into bin starting 
   from 50K and increment of 15K
"""

# necessary modules
import pandas as pd

# read the file 
df = pd.read_csv('Salaries.csv')

df.describe()

# lets get the max salary male professor
max_male_pro = df[(df['sex'] == 'Male') & \
           (df['rank'] == 'Prof') & \
           (df['salary'] == df['salary'].max())
           ]
# max professor in female
max_female_pro = df[(df['sex'] == 'Female') & \
                (df['rank'] == 'Prof')
                ]

# minimum salary in male




print("Max Salary Prof (Male): ",max_male_pro)
print("Max Salary Prof (Female): ",max_female_pro.max())



df[(df['sex'] == 'Female') & \
    ( df['rank'] == "Prof" )
    ]

























