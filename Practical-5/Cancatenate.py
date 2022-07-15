# Program to concatenate two list

A = []
B = []
m = int(input("Enter number of elements in list A: "));
n = int(input("Enter number of elements in list B: "));

for i in range(m):
    element=(input("Enter elements in list A: "))
    A.append(element)

for i in range(n):
    element = (input("Enter elements in list B: "))
    B.append(element)

res = [i + j for i, j in zip(A, B)]

print("The list after element concatenation is : " + str(res))