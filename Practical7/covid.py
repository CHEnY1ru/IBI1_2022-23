import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("E:/desk/")
os.getcwd()
os.listdir()
covid_data = pd.read_csv("full_data.csv")
print(covid_data.head(5))
covid_data.info()
print(covid_data.describe())
print(covid_data.iloc[0,1])
print(covid_data.iloc[2,0:5])
print(covid_data.iloc[0:2,:])
print(covid_data.iloc[0:10:2,0:5])
print(covid_data.iloc[1000::100,])
print(covid_data.iloc[0:3,[0,1,3]])
my_columns = []
print(covid_data.iloc[0:3,my_columns])
print(covid_data.loc[2:4,"date"])
print(covid_data.loc[0:81,"total_cases"])

covid_data.loc[:,"location"]
for i in covid_data.loc[:,"location"]:
    if i=="Afghanistan":
        my_columns.append(True)
    else:
        my_columns.append(False)
print(my_columns)
print(covid_data.loc[my_columns,"total_cases"])
my_columns=[]
for i in covid_data.loc[:,"date"]:
    if i=="2020-03-21":
        my_columns.append(True)
    else:
        my_columns.append(False)
new_location=covid_data.loc[my_columns,"date"]
print(new_location)
new_new_cases=covid_data.loc[my_columns,"new_cases"]
new_new_deaths=covid_data.loc[my_columns,"new_deaths"]
plt.boxplot(new_new_cases)
plt.show()
plt.boxplot(new_new_deaths)
plt.show()
world_dates=covid_data.loc[:,"date"]
world_new_cases=covid_data.loc[:,"new_cases"]
plt.plot(world_dates, world_new_cases, 'yo')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.show()


#answer the question in question.txt
US_columns=[]
for i in covid_data.loc[:,"location"]:
    if i=="United States":
        US_columns.append(True)
    else:
        US_columns.append(False)
US_new_cases=covid_data.loc[US_columns,"new_cases"]
US_total_cases=covid_data.loc[US_columns,"total_cases"]
US_dates=covid_data.loc[US_columns,"date"]
plt.plot(US_dates,US_new_cases,"ro",US_dates,US_total_cases,"bo")
plt.xticks(US_dates.iloc[0::10],fontsize=6)
plt.legend(["new cases","total cases"],fontsize=7)
plt.title("United states Covid 19 cases",fontsize=16)
plt.show()
