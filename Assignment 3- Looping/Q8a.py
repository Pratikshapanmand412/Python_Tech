#a.1! + 2! + 3!.....n!
n = int(input("Enter a number:"))
fact = 1
sum = 0
for i in range(1,n+1):
    fact = fact * i
    sum += fact
print("Result: ",sum)