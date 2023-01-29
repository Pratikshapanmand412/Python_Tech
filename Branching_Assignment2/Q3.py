#WAP to prompt user to enter userid and password .After verifying userid and password
#display a 4 digit random number and ask user to enter the same.If user enters the same 
#then show him success message otherwise failed.(something like captcha)
user_id = input("Enter userid :")
password = int(input("Enter password: "))

if(user_id == "pratiksha") and (password == 12345):
    import random
    x = random.randint(1,9999)
    print(x)

    captcha = int(input("Enter the  given captcha: "))
    if(x == captcha):
         print("Login successful......")
else:
         print("Invalid input")


