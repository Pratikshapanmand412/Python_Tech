#WAP to find sum of following series using functions:
#1! + 2! + 3!.....n!

def fact(n):
    if (n == 0):
        return 1
    else:
        return n * fact(n-1)

def sum():
    sum +=fact(n)
    return sum


n = int(input("Enter a number: "))
print(sum())