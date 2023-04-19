#Question 1
#first, set a function and parameters
def canibuy(house_value,salary):
#use if else method to judge if the house can be paid
    if house_value<=salary*5:
        return print("Yes")
    else:
        return print("No")
canibuy(4,1)
