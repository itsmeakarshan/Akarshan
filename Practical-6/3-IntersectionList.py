# Program to print intersection of two list

list1=[]
list2=[]
list3=[]
m = int(input("Enter number of elements in list1: "));
n = int(input("Enter number of elements in list2: "));

for i in range(m):
    ele1=int(input("Enter element for list1: "))
    list1.append(ele1)

for i in range(n):
    ele2=int(input("Enter element for list2: "))
    list2.append(ele2)

print("Intersection of the given lists is: ")
for i in list1:
    if i in list2:
        list3.append(i)

print(list3)