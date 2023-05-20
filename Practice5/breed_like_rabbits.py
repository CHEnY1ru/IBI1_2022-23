'''pseudocode: first set two variates, one is to judge the generation, one is to show the number of rabbits
then use the while loop to simulate the breeding of the rabbits until the number is over 100
print the result'''
n=1
k=2
#use while loop: while total number of rabbit less than 100 
while k<100:
    #generation plus 1
    n+=1
    #rabbit continue to breed
    k=2*k
#output result
print(f"the generation {n} will over 100 rabbits ")
