# Program to convert binary to decimal

def Binary_to_Decimal(b):
    l = len(b)
    d = 0
    counter = 0
    while (l>0):
        if (b[l-1] != '0' and b[l-1] != '1'):
            print('This is not binary')
            break;
        else:
            s = int(b[l-1]) * (2 ** counter)
            d += s
        l -= 1
        counter += 1
    return (d)

n=int(input("Enter a binary number: "))
print("The decimal equivalent of binary number",n,"is ",Binary_to_Decimal(str(n)))