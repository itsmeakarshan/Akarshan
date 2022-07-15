# Program to find the count of tuple in list

T=[('blood','red'),('leaf','green'),('sky','blue'),('light','white')]

count=0
for i in T:
    if type(i)==tuple:
        count+=1
print("The number of tuples in the given list are ",count)