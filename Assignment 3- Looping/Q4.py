#WAP TO check given number is armstrong or not.
num = int(input("Enter a number: "))
sum = 0
temp = num
n = num
c = 0
while(n > 0):
    c += 1
    n =n// 10
print("Number of digits are: ",c)
while(num > 0):
    r = num % 10
    sum += r ** c
    num //= 10

if(temp == sum):
    print("Number is armstrong")
else:
    print("Number is not armstrong")


