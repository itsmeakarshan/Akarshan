# Program to sort tuple by total digits

def count_digits(tup):
    return sum([len(str(ele)) for ele in tup])

tuple = [(3, 4, 6, 723), (1, 2), (12345,), (134, 234, 34)]

print("The original list is : " + str(tuple))

tuple.sort(key=count_digits)
print("Sorted tuples : " + str(tuple))