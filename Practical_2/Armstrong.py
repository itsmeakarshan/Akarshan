# Python program to check if the number is an Armstrong number or not

num = int(input("Enter a number: "))


sum = 0
c=0

temp1 = num
temp2 = num
while temp1 > 0:
   temp1 //= 10
   c=c+1

while temp2 > 0:
    digit = temp2 % 10
    sum+=digit**c
    temp2 //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
