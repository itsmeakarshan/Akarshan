# Program to count unique values in the list

def count_unique(list):
    count = 0

    freq = {}

    for x in list:
        if (x in freq):
            freq[x] += 1
        else:
            freq[x] = 1

    for key, value in freq.items():
        if value == 1:
            count += 1

    print(count)

list = []
n = int(input("Enter number of elements: "));

for i in range(n):
    element=int(input("Enter elements: "))
    list.append(element)

count_unique(list)