#set variables
costs=[1,8,15,7,5,14,43,40]
#sort
sorted_costs=sorted(costs)
print(sorted_costs)
labels=["Los Angeles1984","Sydney2000","Atlanta1996","Seoul1988",
        "Athens2003","Barcelona1992","London2012","Beijing 2008"]
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
