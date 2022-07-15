# Program to print array elements in reverse order

arr = []
n = int(input("Enter number of elements in array: "));

for i in range(n):
    element=int(input("Enter elements in numerical form: "))
    arr.append(element)

print("The elements in reverse are: ")
for i in range (-1,-n-1,-1):
    print(arr[i])
