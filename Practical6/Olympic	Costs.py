#create a dictionary
dic={1:'Los Angeles 1984',8:'Seoul 1988',15:'Barcelona 1992',
     7:'Atlanta 1996',5:'Sydney 2000',14:'Athens 2003',43:'Beijing 2008',40:'London 2012'}
#set variables
costs=[1,8,15,7,5,14,43,40]
#sort
sorted_costs=sorted(costs)
print(sorted_costs)
labels=[dic[i] for i in costs]
print(labels)
#import numpy and matplotlib
import matplotlib.pyplot as plt
import numpy as np
#change settings
plt.figure(figsize=(10,5))
plt.xticks(fontsize=6)
plt.bar(labels,sorted_costs)
plt.xlabel("olympic_location",color="red")
plt.ylabel("COST")
plt.title("Olympic_Costs",color="pink")
#print barplot
plt.show()
