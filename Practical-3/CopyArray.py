# Program to copy elements of one array into other

arr1 = []
n = int(input("Enter number of elements in array: "));

for i in range(n):
    element=int(input("Enter elements in numerical form: "))
    arr1.append(element)

arr2 = []
for i in range(n):
    arr2.append(arr1[i])

print("The elements of arr2 is: ",arr2)