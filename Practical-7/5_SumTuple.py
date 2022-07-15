# Program to find sum of tuple elements

T = input("Please enter some values:")
tuple = tuple(T.split(" "))

print(tuple)

print("The sum of tuple elements is: ")
sum=0
for i in tuple:
    sum=sum+int(i)

print(sum)