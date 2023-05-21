import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#please change your own path or it may can't run
covid_data = pd.read_csv("full_data.csv")
#correct code for showing the second column from every 100th row from the first 1000 rows
print(covid_data.iloc[0:1001:100,1])
#used a Boolean to show “total cases” for all rows corresponding to Afghanistan.
my_columns = []
for i in covid_data.loc[:,"location"]:
    my_columns.append(i=="Afghanistan")
print(f"Boolean:{my_columns}")

#analyse datas on 31 March 2020
march_column=[]
for date in covid_data.loc[:,"date"]:
    march_column.append(date=="2020-03-31")
new_new_cases=covid_data.loc[march_column,"new_cases"]
new_new_deaths=covid_data.loc[march_column,"new_deaths"]
mean_newcase=np.mean(new_new_cases)
mean_newdeaths=np.mean(new_new_deaths)
print(f"mean of new cases:{mean_newcase},mean od new deaths:{mean_newdeaths}")

#boxplots
plt.boxplot([new_new_cases,new_new_deaths])
plt.xticks(ticks=[1, 2], labels=["New Cases", "New Deaths"])
plt.ylabel("Number")
plt.title("New cases and new deaths on 31 March 2020")
plt.show()

#worldwide
world_data = covid_data[covid_data['location'] == 'World']
world_dates = world_data.loc[:,"date"]
world_new_cases=world_data.loc[:,"new_cases"]
world_new_deaths=world_data.loc[:,"new_deaths"]
plt.plot(world_dates, world_new_cases, 'y-',label='New cases')
plt.plot(world_dates,world_new_deaths,"r-",label="New deaths")
plt.xlabel('Date')
plt.ylabel('Number')
plt.title('New cases and deaths worldwide over Time')
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
plt.plot(US_dates,US_new_cases,"r-",US_dates,US_total_cases,"b-")
plt.xticks(US_dates.iloc[0::10],fontsize=6)
plt.legend(["new cases","total cases"],fontsize=7)
plt.title("United states Covid 19 cases",fontsize=16)
plt.xlabel('Date')
plt.ylabel('Number')
plt.show()
