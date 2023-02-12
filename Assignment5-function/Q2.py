#Sum of all odd numbers between 1 to n.

def odd_no_sum():
    sum = 0
    for i in range(1,n+1,2):
        sum += i 
    print(" Summation of odd numbers: ",sum)

n = int(input("Enter a number: "))
odd_no_sum()