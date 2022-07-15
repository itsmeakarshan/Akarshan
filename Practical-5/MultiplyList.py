# Program to multiply two list

list1=[]
list2=[]
m = int(input("Enter number of elements in lists: "));

for i in range(m):
    ele1=int(input("Enter element for list1: "))
    list1.append(ele1)

for i in range(m):
    ele2=int(input("Enter element for list2: "))
    list2.append(ele2)

mul_list = []
for i in range (m):
    mul_list.append(list1[i] * list2[i])

# printing resultant list
print("Multiplication of list1 and list2 is : " + str(mul_list))