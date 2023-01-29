#Assign two number and swap it without using third variable
x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
x,y=y,x
print("Numbers after swapping: ",x,y)