#first import the numpy and matplotlib, and input the types of movie as labels,and the students number as sizes
#then print a pie chart using matplotlib
#creat a dictory to restore tha table,then print
#craet a variabel as movie genre
#check the genre form the dict and then print

import matplotlib.pyplot as plt
#creat a dictory and set a varable as keyword 
dic_movie={"comedy":73,"Action" :42,
"Romance" :38,
"Fantasy" :28,
"Science-fiction": 22,
"Horror": 19,
"Crime": 18,
"Documentary": 12,
"History": 8,
"War":7}
print(dic_movie)

movie_genre="War"#you can change the type
print(f"number: {dic_movie[movie_genre]}")

#set labels and sizes
labels="comedy","Action" ,"Romance" ,"Fantasy" ,"Science-fiction","Horror","Crime","Documentary","History" ,"War"
sizes=[73,42,38,28,22,19,18,12,8,7]
#print a pie chart
plt.pie(sizes,labels=labels,autopct='%1.1f%%')
plt.show()
