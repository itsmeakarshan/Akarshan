# Program to subtract one list from other

A = []
B = []
m = int(input("Enter number of elements in list A: "));
n = int(input("Enter number of elements in list B: "));

for i in range(m):
    element=int(input("Enter elements in list A: "))
    A.append(element)

for i in range(n):
    element = int(input("Enter elements in list B: "))
    B.append(element)

ans=A.copy()
for i in A:
    if i in B:
        B.remove(i)
        ans.remove(i)

print("A-B: ")
for i in ans:
    print(i,end=' ')

