'''Persudocode: it creates a bar plot using the matplotlib library in Python. 
The code creates a dictionary with the location and cost data. 
It then sorts the data by cost and creates two new lists with the sorted data. 
Finally, it uses matplotlib to create a bar plot with the sorted data'''
#create a dictionary
location=['Los Angeles 1984','Seoul 1988','Barcelona 1992',
     'Atlanta 1996','Sydney 2000','Athens 2003','Beijing 2008','London 2012']
#set variables
costs=[1,8,15,7,5,14,43,40]
#sort
zipped_cost=zip(costs,location)
sorted_zip=sorted(zipped_cost)
new_cost=[i[0] for i in sorted_zip]
new_location=[i[1] for i in sorted_zip]
print(new_cost)
#import numpy and matplotlib
import matplotlib.pyplot as plt
import numpy as np
#change settings
plt.figure(figsize=(10,5))
plt.xticks(fontsize=6)
plt.bar(new_location,new_cost)
plt.xlabel("olympic_location",color="red")
plt.ylabel("COST")
plt.title("Olympic_Costs")
#print barplot
plt.show()
