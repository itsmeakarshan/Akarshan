# Program to find which tuple divisible by k

T = ()
n=int(input("Enter number of elements in tuple: "))

for i in range (n):
    ele=int(input("Enter element: "))
    T=T+(ele,)

k=int(input("Enter value of 'k'"))
print("The elements which are divisible by ",k," are: ")
for i in T:
    if(i%k==0):
        print(i," ",end='')