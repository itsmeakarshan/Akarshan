# Program to print elements at even positions

arr = []
n = int(input("Enter number of elements in array: "));

for i in range(n):
    element=int(input("Enter elements in numerical form: "))
    arr.append(element)

for i in range (0,n,2):
    print("The elements at even positions are: ",arr[i])