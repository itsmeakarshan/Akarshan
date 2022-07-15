# Program to print largest and smallest elements in array

arr = []
n = int(input("Enter number of elements in array: "));

for i in range(n):
    element=int(input("Enter elements in numerical form: "))
    arr.append(element)

max = arr[0]
min = arr[0]
for i in range (n):
    if(arr[i]>max):
        max=arr[i]
    if(arr[i]<min):
        min=arr[i]

print("The largest element in array is: ",max)
print("The smallest element in array is :",min)