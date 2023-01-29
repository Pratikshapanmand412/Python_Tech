#Find the sum of 3 digit number
num=int(input("Enter a 3 digit number: "))
sum=0
sum+=num%10
num//=10
sum+=num%10
num//=10
sum+=num%10
print("Sum of 3 digits of number is :",sum)