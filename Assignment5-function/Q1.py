#WAP to find sum of following series using function:
#1! + 2! + 3!......+ n!

def fact():
    fact=1
    sum = 0
    for i in range (1,n+1):
        fact *= i
        sum += fact
    print("Summation of factorial series:",sum)


n = int(input("Enter number:"))
fact()