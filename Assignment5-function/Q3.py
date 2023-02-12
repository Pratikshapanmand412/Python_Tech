#Sum of all prime numbers between 1 to n.


def prime_no(n):
    for i in range(2,n):
        if n % i == 0:
            break
    else:
         return n + prime_no(n)

n= int(input("Enter a number: "))
prime_numbers=prime_no(n)
print("Sum of all prime numbers :",prime_numbers)
