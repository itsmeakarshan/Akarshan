# Program to merge two list to form dictionary

def merge(keys, values):
  return dict(zip(keys, values))

keys = []
values = []
m = int(input("Enter number of elements: "));

for i in range(m):
    element=(input("Enter string element in list of keys: "))
    keys.append(element)

for i in range(m):
    element = int(input("Enter numerical element in list of values: "))
    values.append(element)

print(merge(keys , values))


