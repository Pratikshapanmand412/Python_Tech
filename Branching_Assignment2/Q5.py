#WAP to check if person is eligible to marry or not (male age>=21 and female age>=18)
gender = input("Enter your gender(f/m):  ")
age = int(input("Enter your age:"))
if(gender == 'f' and age >= 18):
    print("you are eligible to marry...")
elif(gender == 'm' and age >= 21):
    print("You are eligible to marry...")
else:
    print("Invalid input")
