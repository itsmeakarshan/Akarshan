# Program to Sort elements in ascending and descending order

l = []
n = int(input("Enter number of elements in array: "));

for i in range(n):
    element=int(input("Enter elements in numerical form: "))
    l.append(element)

l.sort(reverse=False)
print("Array in ascending order is: ",l)
l.sort(reverse=True)
print("Array in descending order is: ",l)
