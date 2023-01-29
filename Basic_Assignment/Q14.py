#WAP to reverse three digit number
num=int(input("enter a number:"))
rev=0
rev+=num%10
num//=10
rev=rev*10+(num%10)
num//=10
rev=rev*10+(num%10)
num//=10
print("Reverse number is: ",rev)