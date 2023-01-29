#WAP to check if given 3 digit number is a palindrome or not
num = int(input("Enter a number: "))
temp = num
rev = 0
rev += num % 10
num //= 10
rev = rev * 10 + (num % 10)
num //= 10
rev = rev * 10 + (num % 10)
num //= 10

if(rev == temp):
    print("Number is palindrome")
else:
    print("Number is not a palindrome")